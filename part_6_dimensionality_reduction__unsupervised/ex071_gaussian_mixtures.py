from sklearn.mixture import GaussianMixture
from sklearn.datasets import make_blobs

X, y = make_blobs(n_samples=500, centers=3, random_state=42)
gm = GaussianMixture(n_components=3, n_init=10, random_state=42)
gm.fit(X)
print("Gaussian Mixture Model converged:", gm.converged_)
