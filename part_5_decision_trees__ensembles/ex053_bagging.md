# ex053 & ex054: Bagging and Pasting

### Concept
Another way to get an ensemble is to use the **same algorithm** for every predictor but train them on different **random subsets** of the training set.

### Bagging (Bootstrap Aggregating)
Sampling is performed **with replacement** (an instance can be picked multiple times for the same predictor).

### Pasting
Sampling is performed **without replacement**.

### Aggregation
For classification, the ensemble usually uses the **statistical mode** (most frequent vote). For regression, it uses the **average**.

### Why Bagging?
Bagging introduces a bit more diversity in the subsets, resulting in a slightly higher bias but **much lower variance** than pasting. It is the preferred method in most cases.
