# ex018: K-Fold Cross-Validation

### Concept
Measuring accuracy on the training set is a trap. Cross-validation provides a much cleaner estimate of how the model will perform on new data.

### How it works
1. The training set is split into $K$ "folds" (e.g., 3).
2. The model is trained $K$ times. 
3. Each time, it uses $K-1$ folds for training and the remaining fold for evaluation.

### Why Accuracy isn't enough
If only 10% of your images are "5s", a dumb model that always predicts "Not 5" will be 90% accurate. This is why we need more nuanced metrics like Precision and Recall.
