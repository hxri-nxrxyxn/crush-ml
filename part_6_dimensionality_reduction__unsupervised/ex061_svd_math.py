import numpy as np

X = np.random.randn(60, 3)
X_centered = X - X.mean(axis=0)
U, s, Vt = np.linalg.svd(X_centered)
c1 = Vt.T[:, 0]
c2 = Vt.T[:, 1]
print("First two principal components (SVD):\n", c1, "\n", c2)
