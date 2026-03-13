# ex033: Learning Curves

### Concept
How do you tell if your model is overfitting or underfitting? Look at the performance on both the training set and the validation set over time (or as the training set size grows).

### Analysis
- **Underfitting**: Both curves reach a plateau. They are close together but the error is high. (Solution: More complex model or better features).
- **Overfitting**: There is a significant gap between the curves. The model performs much better on training data than on validation data. (Solution: More data or Regularization).
