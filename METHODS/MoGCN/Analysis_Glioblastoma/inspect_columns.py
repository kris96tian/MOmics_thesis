import pandas as pd

# Inspect predictions
predictions = pd.read_csv('result/GCN_predicted_data.csv')
print("Columns in GCN_predicted_data.csv:", predictions.columns.tolist())

# Inspect test_sample
test_sample = pd.read_csv('data/test_sample.csv')
print("Columns in test_sample.csv:", test_sample.columns.tolist())

# Inspect sample_classes
sample_classes = pd.read_csv('data/sample_classes.csv')
print("Columns in sample_classes.csv:", sample_classes.columns.tolist())