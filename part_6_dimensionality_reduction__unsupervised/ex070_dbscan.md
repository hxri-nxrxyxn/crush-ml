# ex070: DBSCAN (Density-Based Spatial Clustering)

### Concept
DBSCAN defines clusters as continuous regions of high density. 

### Why it's better than K-Means
- **Arbitrary Shapes**: It can identify clusters of any shape (not just circles/blobs).
- **Outliers**: It identifies "noise" (points in low-density regions) automatically.
- **No K**: You don't need to specify the number of clusters in advance.

### Parameters
- **`eps`**: The distance to look for neighbors.
- **`min_samples`**: How many neighbors a point needs to be considered a "core point."
