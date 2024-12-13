import pandas as pd
import numpy as np
import torch
import networkx as nx

import matplotlib.pyplot as plt

import sys
sys.path.append('//home/azureuser/MoGCN_br/autoencoder_model.py')
from autoencoder_model import MMAE

fused_matrix = pd.read_csv('result/SNF_fused_matrix.csv', index_col=0)
labels = pd.read_csv('data/sample_classes.csv', index_col=0)
network_data = fused_matrix.join(labels)


graph = nx.from_pandas_adjacency(fused_matrix)
nx.set_node_attributes(graph, labels['class'].to_dict(), 'Subtype')
#for Cytoscape
nx.write_graphml(graph,'result/patient_network.graphml')


## ENRICHMENT


topn_omics_1 = pd.read_csv('/home/azureuser/MoGCN_br/result/topn_omics_1.csv')
unique_genes_topn_omics = pd.unique(topn_omics_1.values.ravel())

unique_genes_df = pd.DataFrame(unique_genes_topn_omics, columns=["Gene"])

output_path = '/home/azureuser/MoGCN_br/result/unique_genes_for_enrichment1.csv'
unique_genes_df.to_csv(output_path, index=False)

topn_omics_2 = pd.read_csv('/home/azureuser/MoGCN_br/result/topn_omics_2.csv')

unique_genes_2 = pd.unique(topn_omics_2.values.ravel())
unique_genes_df_2 = pd.DataFrame(unique_genes_2, columns=["Gene"])
unique_genes_df_2.to_csv('unique_genes_2.csv', index=False)

topn_omics_3 = pd.read_csv('/home/azureuser/MoGCN_br/result/topn_omics_3.csv')
unique_genes_3 = pd.unique(topn_omics_3.values.ravel())
unique_genes_df_3 = pd.DataFrame(unique_genes_3, columns=["Gene"])
unique_genes_df_3.to_csv('unique_genes_3.csv', index=False)
