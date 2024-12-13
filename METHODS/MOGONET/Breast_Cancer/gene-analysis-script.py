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
        'ZNF619', 'BSPRY', 'EPS15', 'NASP', 'TTC39A', 'CELA2A', 'PHLDA3',
        'LAD1', 'CARNS1', 'VPS18', 'CD4', 'TAF12', 'STK3', 'ILF3', 'DDX49',
        'ZZZ3', 'NCKIPSD', 'RAB11FIP5', 'AMFR', 'TYW3', 'RPS27L', 'SPEN', 
        'EEF1A2', 'ARHGAP31', 'DIP2A', 'MIR4695', 'RANBP3', 'IRX5', 'DERL1', 
        'TCIRG1'
    ]
    
    analyzer = GeneAnalyzer(top_genes)    
    analyzer.get_gene_info_from_ncbi()    
    analyzer.plot_gene_distribution()    
    analyzer.generate_report()    

if __name__ == "__main__":
    main()
