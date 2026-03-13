from sklearn.svm import LinearSVR, SVR
import numpy as np

X = 2 * np.random.rand(50, 1)
y = (4 + 3 * X + np.random.randn(50, 1)).ravel()

svm_reg = LinearSVR(epsilon=1.5, random_state=42)
svm_reg.fit(X, y)

print("SVM Regression (LinearSVR) trained.")
