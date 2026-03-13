from sklearn.metrics import precision_recall_curve
import numpy as np

y_true = np.array([0, 0, 1, 1])
y_scores = np.array([0.1, 0.4, 0.35, 0.8])
precisions, recalls, thresholds = precision_recall_curve(y_true, y_scores)

print("Precision-Recall Curve points:")
print("Precisions:", precisions)
print("Recalls:", recalls)
