from sklearn.metrics import precision_recall_curve
import numpy as np

import matplotlib.pyplot as plt

y_true = np.array([0, 0, 1, 1])
y_scores = np.array([0.1, 0.4, 0.35, 0.8])
precisions, recalls, thresholds = precision_recall_curve(y_true, y_scores)

print("Precision-Recall Curve points:")
print("Precisions:", precisions)
print("Recalls:", recalls)

plt.plot(recalls, precisions, "b-", linewidth=2)
plt.xlabel("Recall")
plt.ylabel("Precision")
plt.axis([0, 1, 0, 1])
plt.grid(True)
plt.title("Precision-Recall Curve")
plt.show()
