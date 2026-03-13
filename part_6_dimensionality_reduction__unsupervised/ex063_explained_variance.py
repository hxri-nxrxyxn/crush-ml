from sklearn.decomposition import PCA
import numpy as np

X = np.random.randn(100, 10)
pca = PCA(n_components=5)
pca.fit(X)
print("Explained Variance Ratio of 5 components:", pca.explained_variance_ratio_)
