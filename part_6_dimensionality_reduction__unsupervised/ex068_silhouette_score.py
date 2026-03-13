from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

X, y = make_blobs(n_samples=500, centers=3, random_state=42)
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)
score = silhouette_score(X, kmeans.labels_)
print("Silhouette Score for 3 clusters:", score)
