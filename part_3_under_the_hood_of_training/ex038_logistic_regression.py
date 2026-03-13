from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
import numpy as np

iris = load_iris()
X = iris["data"][:, 3:] # petal width
y = (iris["target"] == 2).astype(np.int32) # Virginica

log_reg = LogisticRegression(solver="lbfgs", random_state=42)
log_reg.fit(X, y)
print("Logistic Regression trained for Iris Virginica.")
print("Probability for 1.7cm width:", log_reg.predict_proba([[1.7]]))
