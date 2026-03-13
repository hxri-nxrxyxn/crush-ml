# ex066: K-Means Clustering

### Concept
K-Means is a simple algorithm capable of clustering unlabeled data into $K$ groups.

### How it works
1. Randomly place $K$ centroids.
2. Label each instance by the nearest centroid.
3. Update centroids by calculating the mean of all instances in each cluster.
4. Repeat until centroids stop moving.

### Characteristics
- It always converges to a solution.
- It might converge to a **local optimum** (a bad solution) depending on the initial centroid placement.
