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
    def generate_report(self, output_file='gene_analysis_report2.md'):
        with open(output_file, 'w') as f:
            f.write("# Gene Analysis Report\n\n")
            f.write(f"## Total Genes Analyzed: {len(self.genes)}\n\n")
            f.write("| Gene Symbol | Chromosome | Description |\n")
            f.write("|------------|------------|-------------|\n")
            
            for gene_symbol, info in self.gene_info.items():
                f.write(f"| {info['symbol']} | {info['chromosome']} | {info['description']} |\n")

def main():
    top_genes = [
        "CARTPT_x", "FABP7_x", "LALBA_x", "S100A7_x", "GSTM1_y", "MUC2_x", "CHGB_x", "PVALB_x", "SCGB1D2_x", 
        "MUCL1_x", "KRT6A_x", "CPB1_x", "DHRS2_x", "CLIC6_y", "KRT15_x", "S100A1_x", "CRABP1_x", "OMD_y", 
        "MUC5B_x", "CLEC3A_x", "S100P_y", "PCSK1_x", "CXCL14_x", "CST5_x", "TFF1_x", "HLA-DRB5_y", "APOD_y", 
        "CYP2A6_x", "CAMP_x", "GLYATL2_x", "CASP14_x", "HBG2_x", "GP2_x", "KRT6B_x", "CALML5_x", "S100A9_y", 
        "CLC_x", "HBG1_x", "RBP5_x", "GSTA1_x", "KRT16_x", "TFF3_x", "PDZK1_x", "PIP_x", "BCAS1_x", 
        "CYP4X1_y", "DNAJC12_y", "PGK2_x", "FGFR2_y", "NCCRP1_x", "VTCN1_x", "GFRA1_y", "SCGN_x", "HMGCS2_x", 
        "PNMT_x", "CSTA_y", "A2ML1_x", "WFDC2_x", "S100A8_y", "HBD_x", "GRB7_x", "TMSB15A_y", "HLA-DRB3", 
        "SERPINB5_x", "CEACAM5_x", "GPD1_x", "HPGD_y", "S100A12_x", "REEP6_y", "GSTT2B_y", "AKR1C2_x", "AKR1B10_x", 
        "LTF_y", "PRTN3_x", "MAPK8IP1_y", "APCS_x", "SCUBE2_y", "PSAT1_y", "MUC6_x", "COMP_y", "FST_y", 
        "DES_x", "NQO1_y", "PLIN4_x", "CRISP3_x", "GSTM3_x", "ADH1B_x", "ITGAE_y", "GDAP1_y", "FCN1_x", 
        "KCTD16_x", "PLA2G2A_x", "PGR_y", "STC2_y", "LGALS7_x", "SCGB2A2_x", "AHSP_x", "VKORC1_y", "OLFM4_x", 
        "PTN_y"
    ]
    
    analyzer = GeneAnalyzer(top_genes)    
    analyzer.get_gene_info_from_ncbi()    
    analyzer.plot_gene_distribution()    
    analyzer.generate_report()    

if __name__ == "__main__":
    main()
