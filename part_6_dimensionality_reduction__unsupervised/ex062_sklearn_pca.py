from sklearn.decomposition import PCA
import numpy as np

X = np.random.randn(100, 3)
pca = PCA(n_components=2)
X2D = pca.fit_transform(X)
print("Original shape:", X.shape, "Projected shape:", X2D.shape)
