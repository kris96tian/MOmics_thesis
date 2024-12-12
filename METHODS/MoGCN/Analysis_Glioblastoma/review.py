import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

predictions = pd.read_csv('result/GCN_predicted_data.csv')
print("Columns in GCN_predicted_data.csv:", predictions.columns.tolist())

sample_classes = pd.read_csv('data/sample_classes.csv')
print("Columns in sample_classes.csv:", sample_classes.columns.tolist())

sample_classes.rename(columns={'Sample_ID': 'Sample', 'class': 'true_label'}, inplace=True)
print("Columns after renaming in sample_classes.csv:", sample_classes.columns.tolist())

merged = pd.merge(predictions, sample_classes[['Sample', 'true_label']], on='Sample')
print("Columns after merging:", merged.columns.tolist())

print("\nMerged DataFrame head:")
print(merged.head())

# classification report
print("\nClassification Report:")
print(classification_report(merged['true_label'], merged['predict_label']))

#  confusion matrix
cm = confusion_matrix(merged['true_label'], merged['predict_label'])
print("Confusion Matrix:\n", cm)

# pl. confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['Class 0', 'Class 1', 'Class 2', 'Class 3'],  
            yticklabels=['Class 0', 'Class 1', 'Class 2', 'Class 3'])  
plt.ylabel('True Label')
plt.xlabel('Predicted Label')
plt.title('Confusion Matrix')

plt.savefig('result/confusion_matrix.png')  
plt.close()  
