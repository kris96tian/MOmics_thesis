import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Paths to raw data files (replace with actual file paths)
omics_paths = {
    "omics1": "rna_seq_ready.csv",
    "omics2": "proteome_ready.csv",
    "omics3": "scnv_ready.csv"
}
labels_path = "labels.csv"  # Path to the labels file

# Preprocess each omics dataset
preprocessed_data = {}
for idx, (omics_name, omics_path) in enumerate(omics_paths.items(), start=1):
    print(f"Processing {omics_name}...")
    # Load raw data (assuming the first column is sample ID)
    data = pd.read_csv(omics_path, index_col=0)
    
    # Transpose the omics data so that samples are rows
    data = data.T  # Transpose to make samples the rows
    
    # Load labels
    labels = pd.read_csv(labels_path, index_col=0)
    print(f"Loaded labels for {omics_name}.")

    # Ensure the samples match in both omics data and labels
    common_samples = data.index.intersection(labels.index)
    
    if len(common_samples) == 0:
        raise ValueError(f"No common sample IDs found between {omics_name} and labels.")
    
    # Align the data based on common sample IDs
    data_aligned = data.loc[common_samples]
    labels_aligned = labels.loc[common_samples]

    # Z-score normalization (standardization)
    scaler = StandardScaler()
    normalized_data = pd.DataFrame(scaler.fit_transform(data_aligned), 
                                    index=data_aligned.index, 
                                    columns=data_aligned.columns)
    
    # Select top 2000 features by variance
    top_features = normalized_data.var(axis=0).nlargest(2000).index
    selected_data = normalized_data[top_features]
    
    # Save feature names (top 2000 features)
    feature_file = f"{idx}_featname.csv"
    pd.DataFrame(top_features).to_csv(feature_file, index=False, header=False)
    print(f"Saved features to {feature_file}.")
    
    # Store preprocessed data for later splitting
    preprocessed_data[omics_name] = selected_data

# Reload labels for splitting (after alignment)
labels = pd.read_csv(labels_path, index_col=0)
print("Loaded labels.")

# Split into training and testing sets using the labels
X_train = {}
X_test = {}
y_train, y_test = train_test_split(labels, test_size=0.3, stratify=labels, random_state=42)

# Save labels for training and testing sets
y_train.to_csv("labels_tr.csv", header=True)  # Save training labels
y_test.to_csv("labels_te.csv", header=True)   # Save testing labels
print("Saved training and testing labels.")

# Save training and testing data for each omics dataset
for idx, (omics_name, data) in enumerate(preprocessed_data.items(), start=1):
    print(f"Splitting and saving {omics_name}...")
    
    # Align the omics data with the labels before splitting
    data_aligned = data.loc[labels.index]
    
    # Split the preprocessed data (training and testing sets) based on the labels
    X_train[omics_name], X_test[omics_name] = train_test_split(
        data_aligned, test_size=0.3, stratify=labels, random_state=42
    )
    
    # Save the training and testing data for each omics dataset
    train_file = f"{idx}_tr.csv"
    test_file = f"{idx}_te.csv"
    X_train[omics_name].to_csv(train_file)
    X_test[omics_name].to_csv(test_file)
    print(f"Saved training data to {train_file} and testing data to {test_file}.")
