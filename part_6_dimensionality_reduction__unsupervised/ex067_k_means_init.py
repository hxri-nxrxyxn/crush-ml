from sklearn.cluster import KMeans
import numpy as np

X = np.random.rand(100, 2)
# Using K-Means++ initialization (default in Sklearn)
kmeans = KMeans(n_clusters=5, init="k-means++", n_init=10, random_state=42)
kmeans.fit(X)
print("K-Means++ initialization logic used.")
