import numpy as np
import pandas as pd
from scipy.stats import ttest_ind
from statsmodels.stats.multitest import multipletests
import os


class MultiOmicsSimulator:
    def __init__(self, n_samples_per_group=(100, 100), seed=42):
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

    def simulate_data(self, include_labels=False):
        feature_names = self._create_feature_names()
        sample_names = [f"Sample_{i}" for i in range(1, self.total_samples + 1)]
        data = {}

        for omic, n_feat in self.n_features.items():
            if omic == "transcriptomics":
                base_data = np.random.poisson(5, (n_feat, self.n_samples_per_group[0]))
                treatment_data = np.random.poisson(5.5, (n_feat, self.n_samples_per_group[1]))
                data[omic] = np.concatenate([base_data, treatment_data], axis=1)
            else:
                data[omic] = np.random.normal(size=(n_feat, self.total_samples))
                data[omic][:, self.n_samples_per_group[0]:] += 0.5

            data[omic] = pd.DataFrame(data[omic], index=feature_names[omic], columns=sample_names)

        metadata = pd.DataFrame({
            "sample_id": sample_names,
            "group": np.repeat(["Control", "Treatment"], self.n_samples_per_group),
            "batch": np.tile(["Batch1", "Batch2"], self.total_samples // 2),
        })

        # Simulate additional labels if requested
        labels = None
        if include_labels:
            np.random.seed(42)
            # Adjusted to allow repetition of class labels
            classes = np.random.choice([0, 1, 2], size=self.total_samples, replace=True)
            labels = pd.DataFrame({
                "sample_id": sample_names,
                "label": classes
            })

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

        quality_metrics = {
            "metabolomics": {
                "rsd": data["metabolomics"].std() / data["metabolomics"].mean(),
                "missing_rate": pd.Series(0, index=data["metabolomics"].index),
                "intensity_range": pd.DataFrame({
                    "min": data["metabolomics"].min(axis=1),
                    "max": data["metabolomics"].max(axis=1),
                }),
            }
        }

        return {
            "data": data,
            "metadata": metadata,
            "feature_info": feature_info,
            "quality_metrics": quality_metrics,
            "labels": labels
        }


class DataAnalyzer:
    @staticmethod
    def check_data_structure(sim_data):
        print("Checking data structure")
        for omic, data in sim_data["data"].items():
            print(f"\n{omic.capitalize()} data: {data.shape[0]} features x {data.shape[1]} samples")
            print(f"Number of NA values: {data.isna().sum().sum()}")
            print(f"Value range: [{data.min().min():.2f}, {data.max().max():.2f}]")
        print(f"\nMetadata: {sim_data['metadata'].shape}")
        print(f"Quality metrics: {list(sim_data['quality_metrics']['metabolomics'].keys())}")

    @staticmethod
    def analyze_metabolomics(sim_data):
        data = sim_data["data"]["metabolomics"]
        metadata = sim_data["metadata"]
        control_samples = metadata["group"] == "Control"
        treatment_samples = metadata["group"] == "Treatment"

        p_values = [
            ttest_ind(data.loc[metabolite, control_samples], data.loc[metabolite, treatment_samples])[1]
            for metabolite in data.index
        ]
        _, p_adj, _, _ = multipletests(p_values, method="fdr_bh")
        significant_features = sum(p_adj < 0.05)

        print(f"Significant metabolites: {significant_features}")
        return {"p_values": p_values, "significant": significant_features}


class DataIO:
    @staticmethod
    def save_multiomics(data_obj, output_dir):
        os.makedirs(output_dir, exist_ok=True)
        for omic, data in data_obj["data"].items():
            data.to_csv(os.path.join(output_dir, f"{omic}_data.csv"))
        data_obj["metadata"].to_csv(os.path.join(output_dir, "metadata.csv"))

        if data_obj.get("labels") is not None:
            data_obj["labels"].to_csv(os.path.join(output_dir, "labels.csv"), index=False)


def main():
    S = MultiOmicsSimulator()
    D = DataAnalyzer()
    IO = DataIO()

    simulated_data = S.simulate_data(include_labels=True)
    D.check_data_structure(simulated_data)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, "Simulated")

    IO.save_multiomics(simulated_data, output_dir)
    print(f"Data saved in directory: {output_dir}")


if __name__ == '__main__':
    main()
