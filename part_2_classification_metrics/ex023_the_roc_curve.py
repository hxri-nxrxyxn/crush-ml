from sklearn.metrics import roc_curve, roc_auc_score
import numpy as np

import matplotlib.pyplot as plt

y_true = np.array([0, 0, 1, 1])
y_scores = np.array([0.1, 0.4, 0.35, 0.8])
fpr, tpr, thresholds = roc_curve(y_true, y_scores)
auc = roc_auc_score(y_true, y_scores)

print("ROC AUC Score:", auc)
print("FPR:", fpr)
print("TPR:", tpr)

plt.plot(fpr, tpr, linewidth=2, label=f"ROC curve (area = {auc:.2f})")
plt.plot([0, 1], [0, 1], 'k--') # dashed diagonal
plt.axis([0, 1, 0, 1])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate (Recall)')
plt.grid(True)
plt.legend(loc="lower right")
plt.title("ROC Curve")
plt.show()
