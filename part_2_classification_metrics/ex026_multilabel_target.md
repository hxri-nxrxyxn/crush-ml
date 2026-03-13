# ex026: Multilabel Classification

### Concept
Sometimes you want your classifier to output multiple labels for each instance. 
*Example:* A face-recognition classifier should identify multiple people in one picture.

### MNIST Example
We train a `KNeighborsClassifier` to output two labels:
1. Is the digit large (7, 8, or 9)?
2. Is the digit odd?

The output for a "7" would be `[True, True]`.
