import numpy as np
from sklearn.cluster import KMeans

# Synthetic RGB image
img = np.random.randint(0, 255, (20, 20, 3))
X = img.reshape(-1, 3)
kmeans = KMeans(n_clusters=8, random_state=42).fit(X)
print("Image segmentation into 8 color clusters complete.")
