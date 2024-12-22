library(omicade4)
library(tidyverse)
library(ade4)   # For ktab 
 

# Dataloading
rna_data <- read.csv("~/GBM/preprocessed/gbm_rnaseq.csv", row.names = 1) 
protein_data <- read.csv("~/GBM/preprocessed/gbm_proteomics.csv", row.names = 1) 
methylation_data <- read.csv("~/GBM/preprocessed/gbm_methylation.csv", row.names = 1)
survival_data <- read.csv("~/GBM/preprocessed/gbm_survival.csv", row.names = 1)
survival_data[is.na(survival_data)] <- 0
metadata <- read.csv("~/GBM/preprocessed/gbm_phenotype.csv", stringsAsFactors = FALSE)

# sample identifiers as rownames
rownames(metadata) <- metadata$idx
metadata$idx <- NULL
metadata$POLE <- ifelse(metadata$POLE == "Yes", "POLE+", "POLE-")
#rownames(metadata) <- gsub("\\.", "-", rownames(metadata))
rownames(metadata)
#colnames(omics_data$mrna) <- gsub("-", "\\.", colnames(omics_data$mrna))


sorted_metadata <- sort(rownames(metadata))
sorted_mrna <- sort(colnames(omics_data$mrna))


omics_data <- list(
  mrna = rna_data,
  protein = protein_data
  methylation = methylation_data
)

str(omics_data)

#############################
mcia_result <- mcia(omics_data)

# Grouping by POLE status
plot(mcia_result, 
     group = metadata$POLE, 
     group.colors = c("red", "blue"), 
     legend = TRUE)

# metadata for specific analyses
relevant_metadata <- metadata[, c("TMB", "WES_purity", "CIBERSORT_B_cell_naive")]  # Replace CIBERSORT_score with an actual column name

#  TMB, WES_purity, and CIBERSORT_B_cell_naive must be numeric
relevant_metadata$TMB <- as.numeric(relevant_metadata$TMB)
relevant_metadata$WES_purity <- as.numeric(relevant_metadata$WES_purity)
relevant_metadata$CIBERSORT_B_cell_naive <- as.numeric(relevant_metadata$CIBERSORT_B_cell_naive)


combined_data <- list(omics_data = omics_data, metadata = relevant_metadata)
relevant_metadata$TMB[is.na(relevant_metadata$TMB) | is.nan(relevant_metadata$TMB) | is.infinite(relevant_metadata$TMB)] <- 0
relevant_metadata$WES_purity[is.na(relevant_metadata$WES_purity) | is.nan(relevant_metadata$TMB) | is.infinite(relevant_metadata$TMB)] <- 0
relevant_metadata$CIBERSORT_B_cell_naive[is.na(relevant_metadata$CIBERSORT_B_cell_naive) | is.nan(relevant_metadata$CIBERSORT_B_cell_naive) | is.infinite(relevant_metadata$CIBERSORT_B_cell_naive)] <- 0

# GENEXPR normalization (log-transformation)
str(omics_data)

sum(is.na(omics_data$mrna)) 
sum(is.na(omics_data$protein))
statis_result <- statis(omics_data)



mrna_data <- as.data.frame(omics_data$mrna)
protein_data <- as.data.frame(omics_data$protein)
omics_list <- list(mrna = mrna_data, protein = protein_data)
ktab_omics <- ktab.list.df(omics_list)

statis_result <- statis(ktab_omics)

########################
summary(statis_result)
plot(statis_result, type = "compromise")



# MFA Analysis
mfa_result <- mfa(ktab_omics)

summary(mfa_result)
plot(mfa_result, type = "global")
plot(mfa_result, type = "individual")
summary(mfa_result)





layout(matrix(1:4, 1, 4))
par(mar=c(2, 1, 0.1, 6))

for (df in omics_data) {
  d <- dist(t(df))
  hcl <- hclust(d)
  dend <- as.dendrogram(hcl)
  plot(dend, horiz=TRUE)
}
  
  
  
  
  
  
  

