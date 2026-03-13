# ex061: SVD Mathematical Foundation

### Concept
Principal Component Analysis (PCA) finds the axis that preserves the maximum amount of variance in the data. To find these axes, we use a matrix factorization technique called **Singular Value Decomposition (SVD)**.

### The Math
SVD decomposes the training set matrix $X$ into the dot product of three matrices:
$$X = U \Sigma V^T$$
The matrix $V$ contains the unit vectors that define all the principal components we are looking for.

### Implementation
In Python, we center the data (subtract the mean) and then use `np.linalg.svd()`. The first $d$ columns of $V$ are the $d$ principal components.
