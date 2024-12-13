library(readr)

methylation_data <- read.csv("gbm_methylation_transposed.csv")  
mRNA_data <- read.csv("gbm_rnaseq_transposed.csv")   
protein_data <- read.csv("gbm_proteomics_transposed.csv")  
survival_data <- read.csv("survival.csv")

survival_data$case_id <- as.character(survival_data$case_id)
#str(survival_data)

survival_data$class <- factor(survival_data$class, levels = c(0, 1))
methylation_case_id <- methylation_data$X
mRNA_case_id <- mRNA_data$X
protein_case_id <- protein_data$X

methylation_expression <- methylation_data[, -1]
mRNA_expression <- mRNA_data[, -1]
protein_expression <- protein_data[, -1]

rownames(methylation_expression) <- methylation_case_id
rownames(mRNA_expression) <- mRNA_case_id
rownames(protein_expression) <- protein_case_id

common_samples <- intersect(survival_data$case_id, rownames(methylation_expression))
methylation_expression <- methylation_expression[common_samples, ]
mRNA_expression <- mRNA_expression[common_samples, ]
protein_expression <- protein_expression[common_samples, ]

survival_data <- survival_data[survival_data$case_id %in% common_samples, ]
methylation_expression <- methylation_expression[match(survival_data$case_id, rownames(methylation_expression)), ]
mRNA_expression <- mRNA_expression[match(survival_data$case_id, rownames(mRNA_expression)), ]
protein_expression <- protein_expression[match(survival_data$case_id, rownames(protein_expression)), ]

# Data Struct
glioblastoma_data <- list(
  data.train = list(
    methylation = methylation_expression[1:round(0.8 * nrow(survival_data)), ],
    mrna = mRNA_expression[1:round(0.8 * nrow(survival_data)), ],
    protein = protein_expression[1:round(0.8 * nrow(survival_data)), ],
    class = survival_data$class[1:round(0.8 * nrow(survival_data))]
  ),
  data.test = list(
    methylation = methylation_expression[(round(0.8 * nrow(survival_data)) + 1):nrow(survival_data), ],
    mrna = mRNA_expression[(round(0.8 * nrow(survival_data)) + 1):nrow(survival_data), ],
    protein = protein_expression[(round(0.8 * nrow(survival_data)) + 1):nrow(survival_data), ],
    class = survival_data$class[(round(0.8 * nrow(survival_data)) + 1):nrow(survival_data)]
  )
)

#str(glioblastoma_data)
save(glioblastoma_data, file = "glioblastoma.RData")

