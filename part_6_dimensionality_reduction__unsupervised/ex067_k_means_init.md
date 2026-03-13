# ex067: K-Means++ and Centroid Initialization

### The Problem
If you place centroids poorly at the start, K-Means will produce sub-optimal clusters.

### Solution: K-Means++
An initialization algorithm that selects centroids that are distant from one another. This greatly reduces the probability of a poor solution. Scikit-Learn uses K-Means++ by default (`init="k-means++"`).

### Inertia
To evaluate a clustering, we measure **Inertia**: the mean squared distance between each instance and its closest centroid. You want low inertia.
