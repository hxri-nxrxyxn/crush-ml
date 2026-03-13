from sklearn.cluster import DBSCAN
from sklearn.datasets import make_moons

X, y = make_moons(n_samples=500, noise=0.05, random_state=42)
dbscan = DBSCAN(eps=0.05, min_samples=5)
dbscan.fit(X)
print("DBSCAN complete. Number of clusters found:", len(set(dbscan.labels_)) - (1 if -1 in dbscan.labels_ else 0))
