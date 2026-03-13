# ex092: Custom Loss Functions

### Concept
Sometimes built-in losses like MSE aren't enough. For example, if you want a loss that is robust to outliers, you might want **Huber Loss**.

### Huber Loss logic
- If the error is small, it acts like MSE (quadratic).
- If the error is large, it acts like MAE (linear).
This prevents large outliers from dominating the training.

### Implementation
You define a Python function that takes `y_true` and `y_pred` and returns a tensor of losses.
