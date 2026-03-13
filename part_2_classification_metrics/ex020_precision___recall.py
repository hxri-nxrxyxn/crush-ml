from sklearn.metrics import precision_score, recall_score, f1_score
import numpy as np

y_true = np.array([True, False, True, True])
y_pred = np.array([True, False, False, True])

print("Precision:", precision_score(y_true, y_pred))
print("Recall:", recall_score(y_true, y_pred))
print("F1 Score:", f1_score(y_true, y_pred))
