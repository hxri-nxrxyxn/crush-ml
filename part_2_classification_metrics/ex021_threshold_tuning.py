from sklearn.model_selection import cross_val_predict
from sklearn.linear_model import SGDClassifier
import numpy as np

X = np.random.randn(1000, 10)
y = (np.random.randn(1000) > 0)
sgd_clf = SGDClassifier(random_state=42)
y_scores = cross_val_predict(sgd_clf, X, y, cv=3, method="decision_function")

threshold = 0
y_pred_with_threshold = (y_scores > threshold)
print("Manual threshold tuning at 0. First 5 predictions:", y_pred_with_threshold[:5])
