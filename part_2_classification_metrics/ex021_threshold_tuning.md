# ex021: Threshold Tuning

### Concept
The SGD classifier computes a score based on a **decision function**. If that score is greater than a threshold, it assigns the instance to the positive class.

### The Tradeoff
- **Raising the threshold**: Increases Precision (you are more picky) but decreases Recall (you miss more 5s).
- **Lowering the threshold**: Increases Recall (you catch more 5s) but decreases Precision (you catch more "fake" 5s).

### Implementation
Use `cross_val_predict` with `method="decision_function"` to get the raw scores, then apply your own logic to select the best threshold.
