from sklearn.model_selection import cross_val_predict
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import SGDClassifier
import numpy as np

X = np.random.randn(1000, 10)
y = (np.random.randn(1000) > 0)
sgd_clf = SGDClassifier(random_state=42)
y_pred = cross_val_predict(sgd_clf, X, y, cv=3)

cm = confusion_matrix(y, y_pred)
print("Confusion Matrix:\n", cm)
