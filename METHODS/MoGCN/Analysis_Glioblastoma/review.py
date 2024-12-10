import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Load predictions
predictions = pd.read_csv('result/GCN_predicted_data.csv')
print("Columns in GCN_predicted_data.csv:", predictions.columns.tolist())

# Load true labels from sample_classes.csv
sample_classes = pd.read_csv('data/sample_classes.csv')
print("Columns in sample_classes.csv:", sample_classes.columns.tolist())

# Rename 'Sample_ID' to 'Sample' and 'class' to 'true_label' for consistency
sample_classes.rename(columns={'Sample_ID': 'Sample', 'class': 'true_label'}, inplace=True)
print("Columns after renaming in sample_classes.csv:", sample_classes.columns.tolist())

# Merge predictions with true labels on the 'Sample' column
merged = pd.merge(predictions, sample_classes[['Sample', 'true_label']], on='Sample')
print("Columns after merging:", merged.columns.tolist())

# Check the first few rows to ensure correct merging
print("\nMerged DataFrame head:")
print(merged.head())

# Generate classification report
print("\nClassification Report:")
print(classification_report(merged['true_label'], merged['predict_label']))

# Generate confusion matrix
cm = confusion_matrix(merged['true_label'], merged['predict_label'])
print("Confusion Matrix:\n", cm)

# Plot confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['Class 0', 'Class 1', 'Class 2', 'Class 3'],  # Update based on your actual classes
            yticklabels=['Class 0', 'Class 1', 'Class 2', 'Class 3'])  # Update based on your actual classes
plt.ylabel('True Label')
plt.xlabel('Predicted Label')
plt.title('Confusion Matrix')

# Save the figure instead of showing it
plt.savefig('result/confusion_matrix.png')  # Save as PNG
# plt.savefig('result/confusion_matrix.pdf')  # Optionally, save as PDF
plt.close()  # Close the figure to free memory