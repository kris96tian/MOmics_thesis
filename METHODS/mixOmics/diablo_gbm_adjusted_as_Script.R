library(mixOmics)
library(tidyverse)
library(survival)
library(survminer)



file_paths <- list(
    rna = "~/GBM/preprocessed/gbm_rnaseq.csv",
    protein = "~/GBM/preprocessed/gbm_proteomics.csv",
    methylation = "~/GBM/preprocessed/gbm_methylation.csv",
    survival = "~/GBM/preprocessed/gbm_survival.csv"
)

# Dataloading
rna_data <- read.csv(file_paths$rna, row.names = 1) %>% t()
protein_data <- read.csv(file_paths$protein, row.names = 1) %>% t()
methylation_data <- read.csv(file_paths$methylation, row.names = 1) %>% t()
survival_data <- read.csv(file_paths$survival, row.names = 1)

# Imputating nans in survival_data
survival_data[is.na(survival_data)] <- 0

common_patients <- Reduce(intersect, list(
  row.names(rna_data),
  row.names(protein_data),
  row.names(methylation_data),
  row.names(survival_data)
))
rna_data <- rna_data[common_patients, ]
protein_data <- protein_data[common_patients, ]
methylation_data <- methylation_data[common_patients, ]
survival_data <- survival_data[common_patients, ]



X <- list(
  mrna = rna_data,
  protein = protein_data,
  methylation = methylation_data
)

row_ids <- rownames(X[[1]])




survival_data$class <- factor(survival_data$class, levels = c(0, 1))
Y <- survival_data$class
str(Y)




# Design-matrix
design <- matrix(c(0, 0.1, 0.1,
                   0.1, 0, 0.1,
                   0.1, 0.1, 0), 
                 nrow = 3, ncol = 3, byrow = TRUE)
rownames(design) <- colnames(design) <- names(X)

ncomp <- 3
test.keepX <- list(
  mrna = seq(10, 100, 10),
  protein = seq(50, 300, 50),
  methylation = seq(10, 100, 10)
)

# DIABLO (tuning)
tuned <- tune.block.splsda(
  X = X,
  Y = Y,
  ncomp = ncomp,
  test.keepX = test.keepX,
  design = design,
  validation = "Mfold",
  folds = 5,
  nrepeat = 10
)

optimal_keepX <- tuned$choice.keepX
print(optimal_keepX)


final.diablo <- block.splsda(
  X = X,
  Y = Y,
  design = design,
  ncomp = ncomp,
  keepX = optimal_keepX
)



# Performance assessment
perf.diablo <- perf(
  final.diablo,
  validation = "Mfold",
  folds = 5,
  nrepeat = 10
)
print(perf.diablo$error.rate)



selected_features <- lapply(names(X), function(block) {
  selectVar(final.diablo, block = block, comp = 1)$name
})
names(selected_features) <- names(X)
print(selected_features)

# Ploting results
plotIndiv(final.diablo, ind.names = FALSE, legend = TRUE, 
          title = "GBM Samples by Survival Groups")

circosPlot(final.diablo, cutoff = 0.7, line.col = "blue")




