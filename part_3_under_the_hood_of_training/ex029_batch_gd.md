# ex029: Batch Gradient Descent

### Concept
Gradient Descent is a generic optimization algorithm. In the **Batch** version, it uses the **entire** training set to compute the gradients at every step.

### Formula
$$\nabla_{\theta} MSE(\theta) = \frac{2}{m} X^T (X\theta - y)$$
$$\theta^{(next step)} = \theta - \eta \nabla_{\theta} MSE(\theta)$$

### Learning Rate ($\eta$)
- **Too low**: The algorithm will eventually converge, but it will take a very long time.
- **Too high**: The algorithm might overshoot the minimum and even diverge (values get larger and larger).

### Pros/Cons
- **Pros**: Guaranteed to find the global minimum for convex functions (like Linear Regression).
- **Cons**: Extremely slow on very large datasets.
