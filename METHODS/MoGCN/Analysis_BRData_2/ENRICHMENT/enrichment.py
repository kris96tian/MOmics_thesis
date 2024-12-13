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
                
                # für gene id
                if 'esearchresult' in search_data and search_data['esearchresult']['count'] > '0':
                    gene_id = search_data['esearchresult']['idlist'][0]
                    
                    summary_params = {
                        "db": "gene",
                        "id": gene_id,
                        "retmode": "json"
                    }
                    
                    summary_response = requests.get(summary_url, params=summary_params)
                    summary_data = summary_response.json()
                    
                    # infos
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
        
        # plots?
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

    ## REPORT
    def generate_report(self, output_file='gene_analysis_report.md'):
        with open(output_file, 'w') as f:
            f.write("# Gene Analysis Report\n\n")
            f.write(f"## Total Genes Analyzed: {len(self.genes)}\n\n")
            f.write("| Gene Symbol | Chromosome | Description |\n")
            f.write("|------------|------------|-------------|\n")
            
            for gene_symbol, info in self.gene_info.items():
                f.write(f"| {info['symbol']} | {info['chromosome']} | {info['description']} |\n")

def main():
    top_genes = [
        'FGF18_x', 'LINC00672_x', 'CD79A_x', 'NBEAL1_x', 'GFRA1_x', 'LINC01354', 'LOC100506136',
        'IFITM10_x', 'CYP4X1_x', 'BMPR1B_x', 'KRT17_x', 'TPRG1_x', 'ESR1_x', 'CEACAM6_x', 'PGR_x',
        'CHRNA5_x', 'SCUBE2_x', 'NPY1R_x', 'LPCAT2_x', 'ADM5_x', 'TCEB3_x', 'S100A8_x', 'CELF6_x',
        'CPT1C_x', 'GRB14_x', 'LRP2_x', 'MT1M_x', 'VPS53_x', 'PLIN5_x', 'PI15_x', 'GABRP_x', 'MAGIX',
        'TNNT1_x', 'AOC2_x', 'MURC_x', 'CFHR3_x', 'LTF_x', 'OBSCN_x', 'PYHIN1_x', 'MTHFD1L_x', 'MGARP_x',
        'AREG_x', 'PROM1_x', 'S100A2_x', 'AKR1E2_x', 'RBFOX2_x', 'APOD_x', 'PRIM1_x', 'TNRC18P1',
        'FBXO10_x', 'CLIC6_x', 'NKAIN1_x', 'ERP27_x', 'PEG10_x', 'S100A9_x', 'LINC00174_x', 'GS1-259H13.2',
        'KIAA1024_x', 'MICALCL_x', 'CLDN15_x', 'ALDH3B2_x', 'C1orf106_x', 'ADCY1_x', 'ZNF660_x',
        'CXCL13_x', 'NHSL2_x', 'RBM20_x', 'MLPH_x', 'CR1_x', 'NCR3LG1_x', 'C1orf95_x', 'NAT1_x',
        'AFF3_x', 'SLPI_x', 'SYT1_x', 'S100P_x', 'HGD_x', 'CIDEC_x', 'NPIPB9_x', 'DACH1_x', 'HBB_x',
        'ADAMTS15_x', 'CCR6_x', 'AQPEP_x', 'TCP10L_x', 'CCDC144A_x', 'NOVA1_x', 'LRG1_x', 'CECR2_x',
        'FBXO46_x', 'ADAM32_x', 'ACRC', 'TRIM29_x', 'MAGED4', 'BTN2A3P_x', 'STC2_x', 'UBD_x', 'FAR2P2',
        'CCL18_x', 'FCRL6_x', 'SHISA2_x', 'KCNE4_x', 'CES3_x', 'KRT23_x', 'SERPINA3_x', 'FGF12_x',
        'TAOK2_x', 'AKR1C1_x', 'HAUS6_x'
    ]
    
    analyzer = GeneAnalyzer(top_genes)    
    analyzer.get_gene_info_from_ncbi()    
    analyzer.plot_gene_distribution()    
    analyzer.generate_report()    

if __name__ == "__main__":
    main()
