from sklearn.decomposition import PCA
import numpy as np

X = np.random.randn(1000, 100)
rnd_pca = PCA(n_components=10, svd_solver="randomized", random_state=42)
X_reduced = rnd_pca.fit_transform(X)
print("Randomized PCA reduction complete. Shape:", X_reduced.shape)
