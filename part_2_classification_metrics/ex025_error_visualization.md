# ex025: Error Analysis and Visualization

### Concept
Instead of just looking at accuracy, we can visualize the confusion matrix as an image to find specific weaknesses.

### Refinement
1. Divide each value in the confusion matrix by the number of images in the corresponding class (Normalization).
2. Fill the diagonal with zeros to keep only the errors.
3. Plot using `matshow()`.

### Insight
If the model often confuses 3s and 5s, the square at (row 3, col 5) will be bright. This tells you that you need better preprocessing or more training data for those specific digits.
