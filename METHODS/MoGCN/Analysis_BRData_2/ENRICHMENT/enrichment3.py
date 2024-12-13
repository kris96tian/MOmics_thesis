import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import json
import time

class GeneAnalyzer:
    def __init__(self, gene_symbols):
        self.genes = gene_symbols
        self.gene_info = {}
    
    def get_gene_info_from_ncbi(self):
        base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
        summary_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
        
        for gene_symbol in self.genes:
            try:
                search_params = {
                    "db": "gene",
                    "term": f"{gene_symbol}[sym] AND human[organism]",
                    "retmode": "json"
                }
                
                search_response = requests.get(base_url, params=search_params)
                search_data = search_response.json()
                
                # Fetch gene id
                if 'esearchresult' in search_data and search_data['esearchresult']['count'] > '0':
                    gene_id = search_data['esearchresult']['idlist'][0]
                    
                    summary_params = {
                        "db": "gene",
                        "id": gene_id,
                        "retmode": "json"
                    }
                    
                    summary_response = requests.get(summary_url, params=summary_params)
                    summary_data = summary_response.json()
                    
                    # Fetch gene information
                    if 'result' in summary_data:
                        gene_info = summary_data['result'][gene_id]
                        self.gene_info[gene_symbol] = {
                            'symbol': gene_symbol,
                            'description': gene_info.get('description', 'No description'),
                            'chromosome': gene_info.get('chromosome', 'Unknown')
                        }
                    
                time.sleep(0.5) 
                
            except Exception as e:
                print(f"Error fetching info for {gene_symbol}: {e}")
                self.gene_info[gene_symbol] = {
                    'symbol': gene_symbol,
                    'description': 'No description',
                    'chromosome': 'Unknown'
                }
    
    def plot_gene_distribution(self):
        chromosomes = [info['chromosome'] for info in self.gene_info.values() 
                       if info['chromosome'] != 'Unknown']
        
        if not chromosomes:
            print("No chromosome data available for plotting.")
            return
        
        plt.figure(figsize=(12, 6))
        chromosome_counts = pd.Series(chromosomes).value_counts()
        
        # Plot distribution
        if not chromosome_counts.empty:
            chromosome_counts.plot(kind='bar')
            plt.title('Distribution of Top Genes Across Chromosomes')
            plt.xlabel('Chromosome')
            plt.ylabel('Number of Genes')
            plt.tight_layout()
            plt.savefig('chromosome_distribution.png')
            plt.close()
        else:
            print("No valid chromosome data to plot.")

    ## Generate Report
    def generate_report(self, output_file='gene_analysis_report3.md'):
        with open(output_file, 'w') as f:
            f.write("# Gene Analysis Report\n\n")
            f.write(f"## Total Genes Analyzed: {len(self.genes)}\n\n")
            f.write("| Gene Symbol | Chromosome | Description |\n")
            f.write("|------------|------------|-------------|\n")
            
            for gene_symbol, info in self.gene_info.items():
                f.write(f"| {info['symbol']} | {info['chromosome']} | {info['description']} |\n")

def main():
    top_genes = [
        "PGAP3", "CDK12", "MIR4728", "IKZF3", "ERBB2", "MIEN1_y", "GRB7_y", "PNMT_y", "MED1_y", "NEUROD2",
        "TCAP", "LRRC3C", "WASH3P_y", "GSDMA", "STARD3", "PPP1R1B_y", "PSMD3", "ORMDL3", "DDX11L9", "GSDMB",
        "UNC93B6", "CACNB1", "FBXL20_y", "CSF3", "ZPBP2", "MED24", "ANO1", "RHPN2", "NADSYN1", "RPL19",
        "LRRC37A11P", "C17orf98", "MIR4727", "GPATCH1", "ANKRD30BP2", "FBXO47", "ARL5C", "GPR179", "MIR4734",
        "SNORA21|ENSG00000252699.1", "ANKRD20A11P", "CYP4F29P", "TLX1NB", "STAC2", "PCGF2_y", "EIF4EBP1_y", "SNORD124",
        "POTED", "LASP1", "MIR4726", "PSMB3", "ERLIN2", "LSM1_y", "TEKT4P2_y", "ARHGAP23", "THRA",
        "SNORA70|ENSG00000252199.1", "RNA5SP488", "FGF3", "GPR124", "LINC00672_y", "RPL23", "ADRB3", "MRPL45",
        "MIR3648", "RAB11FIP1", "BRF2", "PLXDC1", "FGFR1", "RN7SL102P", "ZNF703", "TACC1", "MLLT6", "PIP4K2B",
        "PLEKHA2", "SRCIN1", "SNORD38|ENSG00000207199.1", "SNORA21|ENSG00000199293.1", "UNC5D", "STAR", "RPS20P22",
        "CWC25", "WHSC1L1", "LIPI", "TNN_y", "PPAPDC1B", "BAGE2", "C17orf96", "RNA5SP264", "LETM2", "LBX1",
        "RN7SL52P", "CRYBA1", "RN7SL458P", "SOCS7_y", "PREX2", "KCNU1", "RN7SL709P", "PROSC", "BAG4_y"
    ]
    
    analyzer = GeneAnalyzer(top_genes)    
    analyzer.get_gene_info_from_ncbi()    
    analyzer.plot_gene_distribution()    
    analyzer.generate_report()    

if __name__ == "__main__":
    main()
