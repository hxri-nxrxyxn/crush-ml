from sklearn.metrics import confusion_matrix
import numpy as np
import matplotlib.pyplot as plt

y_true = [0, 1, 2, 2, 0]
y_pred = [0, 2, 1, 2, 0]
conf_mx = confusion_matrix(y_true, y_pred)

# Normalizing by row to see error rates
row_sums = conf_mx.sum(axis=1, keepdims=True)
norm_conf_mx = conf_mx / row_sums
np.fill_diagonal(norm_conf_mx, 0)

print("Normalized Confusion Matrix (focus on errors):\n", norm_conf_mx)

plt.matshow(norm_conf_mx, cmap=plt.cm.gray)
plt.show()
