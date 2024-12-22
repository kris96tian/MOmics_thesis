import streamlit as st
import mofax as mfx
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import tempfile
import warnings
import numpy as np
import seaborn as sns
from gprofiler import GProfiler

warnings.filterwarnings("ignore")

st.set_page_config(
    page_title="MOFA+ Model Explorer",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    /* Styling omitted for brevity */
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="custom-title">
        <h1 style='margin:0'>MOFA+ Model Explorer</h1>
        <p style='margin:0;opacity:0.8;font-size:1.1em'>Analyze and visualize multi-omics factor analysis results</p>
    </div>
""", unsafe_allow_html=True)

st.set_page_config(
    page_title="MOFA+ Model Explorer",
    layout="wide",
    initial_sidebar_state="expanded"
)

with st.sidebar:
    st.markdown("### Model Configuration")
    model_file = st.file_uploader("Upload MOFA+ Model (.hdf5)", type=["hdf5"])
    if st.button("Run Glioblastoma Model"):
        model_file = "model.hdf5"  
    if st.button("Run Breast Cancer Model"):
        model_file = "brmodel.hdf5"  

def process_mofa_weights(model):
    weights = model.get_weights()
    weights_df = pd.DataFrame(weights)
    return weights_df

def get_top_features(weights_df, n_features=30):
    top_features = {}
    for factor in range(weights_df.shape[1]):
        abs_weights = np.abs(weights_df.iloc[:, factor])
        top_indices = abs_weights.nlargest(n_features).index
        top_features[f"Factor_{factor+1}"] = top_indices.tolist()
    return top_features

def run_enrichment(features_dict):
    gp = GProfiler(return_dataframe=True)
    all_results = []
    
    for factor, genes in features_dict.items():
        try:
            results = gp.profile(
                query=genes,
                organism='hsapiens',
                sources=['GO:BP', 'KEGG', 'REAC'],
                user_threshold=0.05
            )
            results['factor'] = factor
            results['neglog10pval'] = -np.log10(results['p_value'])
            all_results.append(results)
        except Exception as e:
            st.error(f"Error in enrichment for {factor}: {str(e)}")
    
    if all_results:
        return pd.concat(all_results, ignore_index=True)
    return pd.DataFrame()

def plot_enrichment(factor, results, top_n=10):
    if len(results) == 0:
        st.warning(f"No significant enrichment for {factor}")
        return
    
    factor_results = results[results['factor'] == factor]
    if len(factor_results) == 0:
        st.warning(f"No significant enrichment for {factor}")
        return
    
    fig, ax = plt.subplots(figsize=(12, 6))
    plot_df = factor_results.nsmallest(top_n, 'p_value')
    
    sns.barplot(data=plot_df,
                y='name',
                x='neglog10pval',
                color='steelblue',
                ax=ax)
    
    plt.title(f'Enrichment Results - {factor}')
    plt.xlabel('-log10(p-value)')
    plt.tight_layout()
    return fig

if model_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".hdf5") as tmp_file:
        if isinstance(model_file, str): 
            temp_filepath = model_file
        else:
            tmp_file.write(model_file.read())
            temp_filepath = tmp_file.name

    m = mfx.mofa_model(temp_filepath)

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"<div class='metric-container'><div class='metric-label'>Total Cells</div><div class='metric-value'>{m.shape[0]:,}</div></div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"<div class='metric-container'><div class='metric-label'>Features</div><div class='metric-value'>{m.shape[1]:,}</div></div>", unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"<div class='metric-container'><div class='metric-label'>Groups</div><div class='metric-value'>{len(m.groups)}</div></div>", unsafe_allow_html=True)

    with st.sidebar:
        st.markdown("### Analysis Parameters")
        selected_factor = st.selectbox("Select Factor", m.factors)
        n_features = st.slider("Number of Features to Display", 
                             min_value=1, 
                             max_value=20, 
                             value=5,
                             help="Adjust the number of features shown in visualizations")

        st.markdown("### Export Options")
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("📥 Weights Data"):
                weights_df = m.get_weights(df=True)
                csv = weights_df.to_csv(index=False)
                st.download_button(
                    label="Download CSV",
                    data=csv,
                    file_name='weights_data.csv',
                    mime='text/csv',
                )
        
        with col2:
            if st.button("📊 Variance Data"):
                variance_df = m.calculate_variance_explained()
                csv = variance_df.to_csv(index=False)
                st.download_button(
                    label="Download CSV",
                    data=variance_df.to_csv(index=False),
                    file_name='variance_explained.csv',
                    mime='text/csv',
                )

    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Feature Weights", "Ranked Weights", "Variance Analysis", "Correlation Matrix", "Enrichment Analysis"])

    with tab1:
        st.markdown("### Top Feature Weights")
        with st.container():
            ax_weights = mfx.plot_weights_heatmap(m, n_features=10)
            plt.tight_layout()
            st.pyplot(ax_weights.figure)

    with tab2:
        st.markdown("### Ranked Weights")
        try:
            nf = 2  
            f, axarr = plt.subplots(nf, nf, figsize=(10,10))
            fnum = 0
            for i in range(nf):
                for j in range(nf):
                    mfx.plot_weights_ranked(m, factor=fnum, ax=axarr[i][j], n_features=10, x_rank_offset=50, y_repel_coef=0.05, attract_to_points=False)
                    fnum += 1
            plt.tight_layout()
            st.pyplot()
        except Exception as e:
            st.error(f"Failed to plot ranked weights: {str(e)}")

    with tab3:
        st.markdown("### Variance Explained Analysis")
        variance_df = m.get_r2(factors=list(range(2))).sort_values("R2", ascending=False)
        st.dataframe(variance_df)

    with tab4:
        st.markdown("### Factor Correlation Analysis (Pearson)")
        correlation_matrix = m.get_weights(df=True).corr()
        mfx.plot_factors_correlation(m)
        plt.title("Pearson r")
        st.pyplot()

    with tab5:
        st.markdown("### Enrichment Analysis")        
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                n_features = st.slider(
                    "Number of top features for enrichment",
                    min_value=10,
                    max_value=100,
                    value=30,
                    step=5,
                    help="Select how many top features to include in the enrichment analysis"
                )
            with col2:
                top_n_results = st.slider(
                    "Number of enrichment results to display per plot",
                    min_value=5,
                    max_value=20,
                    value=10,
                    step=1,
                    help="Select how many enrichment results to display in each factor plot"
                )

        if st.button("Run Enrichment Analysis", key="run_enrichment"):
            with st.spinner("Running enrichment analysis..."):
                try:
                    weights_df = process_mofa_weights(m)
                    top_features = get_top_features(weights_df, n_features=n_features)
                    enrichment_results = run_enrichment(top_features)

                    if not enrichment_results.empty:
                        st.subheader("Factor-Specific Enrichment Plots")
                        for factor in top_features.keys():
                            fig = plot_enrichment(factor, enrichment_results, top_n=top_n_results)
                            if fig:
                                st.pyplot(fig)
                            st.markdown("---")

                        st.subheader("Complete Enrichment Results")

                        with st.expander("Filter and Sort Options"):
                            col1, col2 = st.columns(2)
                            with col1:
                                selected_factors = st.multiselect(
                                    "Filter by Factor",
                                    options=enrichment_results['factor'].unique(),
                                    default=enrichment_results['factor'].unique()
                                )
                            with col2:
                                selected_sources = st.multiselect(
                                    "Filter by Source",
                                    options=enrichment_results['source'].unique(),
                                    default=enrichment_results['source'].unique()
                                )

                        filtered_results = enrichment_results[
                            (enrichment_results['factor'].isin(selected_factors)) &
                            (enrichment_results['source'].isin(selected_sources))
                        ]

                        st.dataframe(
                            filtered_results[['factor', 'source', 'name', 'p_value', 'neglog10pval']]
                            .sort_values(['factor', 'p_value'])
                        )

                        csv = filtered_results.to_csv(index=False)
                        st.download_button(
                            label="Download Results CSV",
                            data=csv,
                            file_name='enrichment_results.csv',
                            mime='text/csv',
                        )
                    else:
                        st.warning("No significant enrichment results found for any factor.")
                except Exception as e:
                    st.error(f"An error occurred during enrichment analysis: {str(e)}")
else:
    st.markdown("""
        <div style="text-align: center; padding: 4rem 2rem;">
            <div style="font-size: 4rem; margin-bottom: 1rem;">📊</div>
            <h2 style="color: #1a1f36; margin-bottom: 1rem;">Welcome to MOFA+ Model Explorer</h2>
            <p style="color: #6b7280; font-size: 1.1em;">Please upload a MOFA+ .hdf5 file using the sidebar to begin your analysis.</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("""
        ---
        **Created by Kristian Alikaj**  
        For more, visit [My GitHub](https://github.com/kris96tian) or [My Portfolio Website](https://kris96tian.github.io/)
""")
