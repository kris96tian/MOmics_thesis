import numpy as np
import pandas as pd
from scipy.stats import ttest_ind
from statsmodels.stats.multitest import multipletests
import os
from sklearn.preprocessing import StandardScaler
import sys


class MultiOmicsSimulator:
    def __init__(self, n_samples_per_group=(100, 100, 100), seed=42):
        np.random.seed(seed)
        self.n_samples_per_group = n_samples_per_group
        self.total_samples = sum(n_samples_per_group)
        self.n_features = {
            "transcriptomics": 3234,
            "proteomics": 2187,
            "metabolomics": 129,
            "methylation": 1110,
        }

    def _create_feature_names(self):
        feature_names = {}
        for omic, n_feat in self.n_features.items():
            if omic == "transcriptomics":
                feature_names[omic] = [f"ENSG{str(i).zfill(11)}" for i in range(1, n_feat + 1)]
            elif omic == "proteomics":
                feature_names[omic] = [f"PROT{str(i).zfill(6)}" for i in range(1, n_feat + 1)]
            elif omic == "metabolomics":
                feature_names[omic] = [f"HMDB{str(i).zfill(7)}" for i in range(1, n_feat + 1)]
            elif omic == "methylation":
                feature_names[omic] = [f"cg{str(i).zfill(8)}" for i in range(1, n_feat + 1)]
        return feature_names

    def _normalize_data(self, data):
        """
        Normalize data using min-max scaling to [0, 1] range
        
        Parameters:
        -----------
        data : np.ndarray
            Input data array
        
        Returns:
        --------
        np.ndarray
            Normalized data
        """
        return (data - data.min(axis=0)) / (data.max(axis=0) - data.min(axis=0) + 1e-8)

    def _standardize_data(self, data):
        """
        Standardize data to zero mean and unit variance
        
        Parameters:
        -----------
        data : np.ndarray
            Input data array
        
        Returns:
        --------
        np.ndarray
            Standardized data
        """
        scaler = StandardScaler()
        return scaler.fit_transform(data)

    def simulate_data(self):
        feature_names = self._create_feature_names()
        sample_names = [f"Sample_{i}" for i in range(1, self.total_samples + 1)]
        data = {}

        for omic, n_feat in self.n_features.items():
            if omic == "transcriptomics":
                base_data = np.random.poisson(5, (n_feat, self.n_samples_per_group[0]))
                treatment1_data = np.random.poisson(5.5, (n_feat, self.n_samples_per_group[1]))
                treatment2_data = np.random.poisson(6.0, (n_feat, self.n_samples_per_group[2]))
                omic_data = np.concatenate([base_data, treatment1_data, treatment2_data], axis=1).T
            else:
                base_data = np.random.normal(0, 1, (self.n_samples_per_group[0], n_feat))
                treatment1_data = np.random.normal(0.5, 1, (self.n_samples_per_group[1], n_feat))
                treatment2_data = np.random.normal(1.0, 1, (self.n_samples_per_group[2], n_feat))
                
                omic_data = np.concatenate([base_data, treatment1_data, treatment2_data], axis=0)
            
            omic_data_normalized = self._normalize_data(omic_data)
            omic_data_standardized = self._standardize_data(omic_data_normalized)
            
            data[omic] = pd.DataFrame(
                omic_data_standardized, 
                columns=feature_names[omic], 
                index=sample_names
            )
        metadata = pd.DataFrame({
            "sample_id": sample_names,
            "group": np.repeat(["Control", "Treatment1", "Treatment2"], self.n_samples_per_group),
            "batch": np.tile(["Batch1", "Batch2", "Batch3"], self.total_samples // 3),
        }, index=sample_names)

        metabolite_n = self.n_features["metabolomics"]
        feature_info = {
            "metabolomics": pd.DataFrame({
                "metabolite_id": feature_names["metabolomics"],
                "metabolite_name": [f"Metabolite_{i}" for i in range(1, metabolite_n + 1)],
                "class": np.random.choice(
                    ["Amino_acid", "Lipid", "Carbohydrate", "Nucleotide", "Unknown"], metabolite_n
                ),
                "mz": np.round(np.random.uniform(50, 1000, metabolite_n), 4),
                "rt": np.round(np.random.uniform(0.5, 20, metabolite_n), 2),
            })
        }

        # qc
        quality_metrics = {
            "metabolomics": {
                "rsd": data["metabolomics"].std(),
                "missing_rate": pd.Series(0, index=data["metabolomics"].columns),
                "intensity_range": pd.DataFrame({
                    "min": data["metabolomics"].min(),
                    "max": data["metabolomics"].max(),
                }),
            }
        }
        labels = self._generate_labels(sample_names)

        return {
            "data": data,
            "metadata": metadata,
            "feature_info": feature_info,
            "quality_metrics": quality_metrics,
            "labels": labels
        }

    def _generate_labels(self, sample_names):
        """
        Generate labels with different distributions across groups
        
        Parameters:
        -----------
        sample_names : list
            List of sample names
        
        Returns:
        --------
        pd.DataFrame
            DataFrame with sample IDs and corresponding labels
        """
        np.random.seed(42)
        labels = pd.DataFrame({
            "sample_id": sample_names,
            "label": np.concatenate([
                np.random.choice(["Low", "Medium", "High"], size=self.n_samples_per_group[0], 
                                  p=[0.6, 0.3, 0.1]),  # Control group
                np.random.choice(["Low", "Medium", "High"], size=self.n_samples_per_group[1], 
                                  p=[0.2, 0.5, 0.3]),  # Treatment1 group
                np.random.choice(["Low", "Medium", "High"], size=self.n_samples_per_group[2], 
                                  p=[0.1, 0.3, 0.6])   # Treatment2 group
            ])
        }, index=sample_names)
        return labels


class DataAnalyzer:
    @staticmethod
    def check_data_structure(sim_data):
        """
        Print detailed information about the simulated data structure
        
        Parameters:
        -----------
        sim_data : dict
            Simulated multi-omics data dictionary
        """
        print("Checking data structure")
        for omic, data in sim_data["data"].items():
            print(f"\n{omic.capitalize()} data: {data.shape[1]} features x {data.shape[0]} samples")
            print(f"Number of NA values: {data.isna().sum().sum()}")
            print(f"Value range: [{data.min().min():.2f}, {data.max().max():.2f}]")
            print("Column names (first 5):", list(data.columns)[:5])
        
        print(f"\nMetadata: {sim_data['metadata'].shape}")
        print(f"Quality metrics: {list(sim_data['quality_metrics']['metabolomics'].keys())}")
        print(f"\nLabels: {sim_data['labels'].shape}")
        print(f"Label distribution:\n{sim_data['labels']['label'].value_counts()}")
        
        for omic, data in sim_data["data"].items():
            print(f"\n{omic.capitalize()} data statistics:")
            print("Mean per feature:", data.mean().describe())
            print("Std per feature:", data.std().describe())


class DataIO:
    @staticmethod
    def save_multiomics(data_obj, output_dir):
        """
        Save multi-omics data to CSV files
        
        Parameters:
        -----------
        data_obj : dict
            Multi-omics data dictionary
        output_dir : str
            Directory to save output files
        """
        os.makedirs(output_dir, exist_ok=True)
        
        for omic, data in data_obj["data"].items():
            data.to_csv(os.path.join(output_dir, f"{omic}_data.csv"))
        data_obj["metadata"].to_csv(os.path.join(output_dir, "metadata.csv"))
        data_obj["labels"].to_csv(os.path.join(output_dir, "labels.csv"))


def main():
    """
    Main function to simulate and save multi-omics data
    """
    S = MultiOmicsSimulator()
    D = DataAnalyzer()
    IO = DataIO()
    
    simulated_data = S.simulate_data()
    D.check_data_structure(simulated_data)
    
    output_dir = os.path.expanduser("/mnt/chromeos/MyFiles/Simulated")
    output_dir = input("Enter output directory path: ").strip()
    if not output_dir:
        output_dir = os.getcwd()
        print(f"No directory entered. Using current directory: {output_dir}")
    
    IO.save_multiomics(simulated_data, output_dir)


if __name__ == '__main__':
    main()
