import pandas as pd
import gseapy as gp
import matplotlib.pyplot as plt

# Gene list with scores
gene_data = {
    "Gene": [
        "CA12", "THSD4", "TBC1D9", "GFRA1", "IL6ST", "ESR1", "DACH1", "MLPH", "XBP1", 
        "PGR", "CCNE1", "ZG16B", "PSAT1", "ENO1", "SCUBE2", "CPEB2", "PFKP", "ACADSB", 
        "DNAJC12", "ANKRA2"
    ],
    "Score": [
        0.39819579, 0.39715330, 0.35756746, 0.35596854, 0.27958475, 0.27086995, 0.24358524, 
        0.23282021, 0.20413719, 0.19682065, -0.16859947, 0.16362949, -0.12102384, -0.07353477, 
        0.06869528, 0.03590851, -0.03246028, 0.02385063, 0.02111726, 0.01795270
    ]
}


df = pd.DataFrame(gene_data)
upregulated = df[df['Score'] > 0]['Gene'].tolist()
downregulated = df[df['Score'] < 0]['Gene'].tolist()

# upregulated genes
enrichr_up = gp.enrichr(gene_list=upregulated,
                        gene_sets='KEGG_2021_Human',  
                        organism='Human', 
                        outdir='enrichr_up_results', 
                        cutoff=0.05)  

# downregulated genes
enrichr_down = gp.enrichr(gene_list=downregulated,
                          gene_sets='KEGG_2021_Human',  
                          organism='Human', 
                          outdir='enrichr_down_results', 
                          cutoff=0.05)

enrichr_up.results.to_csv("/home/azureuser/PROJECTS_ALL/MIX_BR/upregulated_enrichment_results.csv", index=False)
enrichr_down.results.to_csv("/home/azureuser/PROJECTS_ALL/MIX_BR/downregulated_enrichment_results.csv", index=False)

def plot_enrichment_results(results, title, output_file):
    top_results = results.head(10)  
    plt.figure(figsize=(10, 6))
    plt.barh(top_results['Term'], top_results['Combined Score'], color='skyblue')
    plt.xlabel('Combined Score')
    plt.title(title)
    plt.gca().invert_yaxis()  
    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()

plot_enrichment_results(enrichr_up.results, "Top Enriched Pathways (Upregulated Genes)", "/home/azureuser/PROJECTS_ALL/MIX_BR/upregulated_enrichment_plot.png")
plot_enrichment_results(enrichr_down.results, "Top Enriched Pathways (Downregulated Genes)", "/home/azureuser/PROJECTS_ALL/MIX_BR/downregulated_enrichment_plot.png")
