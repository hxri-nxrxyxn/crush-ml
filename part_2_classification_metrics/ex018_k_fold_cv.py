from sklearn.model_selection import cross_val_score
from sklearn.linear_model import SGDClassifier
import numpy as np

# Load small subset for CV demo
X = np.random.randn(1000, 10)
y = (np.random.randn(1000) > 0)
sgd_clf = SGDClassifier(random_state=42)

scores = cross_val_score(sgd_clf, X, y, cv=3, scoring="accuracy")
print("Cross-Validation Accuracy Scores:", scores)
