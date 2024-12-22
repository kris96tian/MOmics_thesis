import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

omics_paths = {
    "omics1": "/workspaces/env/simul/Simulated/transcriptomics_data.csv",
    "omics2": "/workspaces/env/simul/Simulated/proteomics_data.csv",
    "omics3": "/workspaces/env/simul/Simulated/methylation_data.csv"
}
labels_path = "/workspaces/env/simul/Simulated/labels.csv" 


preprocessed_data = {}
for idx, (omics_name, omics_path) in enumerate(omics_paths.items(), start=1):
    print(f"Processing {omics_name}...")

    data = pd.read_csv(omics_path, index_col=0).T
    labels = pd.read_csv(labels_path, index_col=0)  # Load labels
    print(f"Loaded labels for {omics_name}.")


    if data.shape[0] != labels.shape[0]:
        print(f"Mismatch in sample sizes between {omics_name} data and labels.")
        data = data.loc[labels.index]
    
    # Z-score normalization (standardization)
    scaler = StandardScaler()
    normalized_data = pd.DataFrame(scaler.fit_transform(data), 
                                    index=data.index, 
                                    columns=data.columns)
    
    # top 2000 features by var.
    top_features = normalized_data.var(axis=0).nlargest(2000).index
    selected_data = normalized_data[top_features]  
    feature_file = f"{idx}_featname.csv"
    pd.DataFrame(top_features).to_csv(feature_file, index=False, header=False)
    print(f"Saved features to {feature_file}.")
    preprocessed_data[omics_name] = selected_data

labels = pd.read_csv(labels_path, index_col=0)  # Ensure we reload labels after potential alignment
print("Loaded labels.")



# Splitting . . .
X_train = {}
X_test = {}
y_train, y_test = train_test_split(labels, test_size=0.3, stratify=labels, random_state=42)


y_train.to_csv("labels_tr.csv", header=True) 
y_test.to_csv("labels_te.csv", header=True)   
print("Saved training and testing labels.")


for idx, (omics_name, data) in enumerate(preprocessed_data.items(), start=1):
    print(f"Splitting and saving {omics_name}...")
    data_aligned = data.loc[labels.index]
    X_train[omics_name], X_test[omics_name] = train_test_split(
        data_aligned, test_size=0.3, stratify=labels, random_state=42
    )
    train_file = f"{idx}_tr.csv"
    test_file = f"{idx}_te.csv"
    X_train[omics_name].to_csv(train_file)
    X_test[omics_name].to_csv(test_file)
    print(f"Saved training data to {train_file} and testing data to {test_file}.")
