from sklearn.metrics import roc_curve, roc_auc_score
import numpy as np

y_true = np.array([0, 0, 1, 1])
y_scores = np.array([0.1, 0.4, 0.35, 0.8])
fpr, tpr, thresholds = roc_curve(y_true, y_scores)
auc = roc_auc_score(y_true, y_scores)

print("ROC AUC Score:", auc)
print("FPR:", fpr)
print("TPR:", tpr)
