library(readr)

scnv_data <- read.csv("/home/azureuser/PROJECTS_ALL/MIX_BR/scnv.csv")  
mRNA_data <- read.csv("/home/azureuser/PROJECTS_ALL/MIX_BR/transcr.csv")   
protein_data <- read.csv("/home/azureuser/PROJECTS_ALL/MIX_BR/proteome.csv")  
clin_data <- read.csv("/home/azureuser/PROJECTS_ALL/MIX_BR/clinical.csv")

clin_data$SampleID <- as.character(clin_data$SampleID)
#str(survival_data)

clin_data$PAM50 <- factor(clin_data$PAM50, levels = c(0,1,2,3))
scnv_id <- clin_data$SampleID
mRNA_id <- clin_data$SampleID
protein_id <- clin_data$SampleID

scnv_expression <- scnv_data[, -1]
mRNA_expression <- mRNA_data[, -1]
protein_expression <- protein_data[, -1]



rownames(scnv_expression) <- scnv_id
rownames(mRNA_expression) <- mRNA_id
rownames(protein_expression) <- protein_id


# Data Struct
bcancerdata <- list(
  data.train = list(
    scnv = scnv_expression[1:round(0.8 * nrow(clin_data)), ],
    mrna = mRNA_expression[1:round(0.8 * nrow(clin_data)), ],
    protein = protein_expression[1:round(0.8 * nrow(clin_data)), ],
    class = clin_data$PAM50[1:round(0.8 * nrow(clin_data))]
  ),
  data.test = list(
    scnv = scnv_expression[(round(0.8 * nrow(clin_data)) + 1):nrow(clin_data), ],
    mrna = mRNA_expression[(round(0.8 * nrow(clin_data)) + 1):nrow(clin_data), ],
    protein = protein_expression[(round(0.8 * nrow(clin_data)) + 1):nrow(clin_data), ],
    class = clin_data$PAM50[(round(0.8 * nrow(clin_data)) + 1):nrow(clin_data)]
  )
)

#str(glioblastoma_data)
save(bcancerdata, file = "/home/azureuser/PROJECTS_ALL/MIX_BR/bcancerdata.RData")

