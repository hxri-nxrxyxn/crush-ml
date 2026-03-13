# ex034: Ridge Regression (L2 Regularization)

### Concept
Regularization reduces overfitting by constraining the model. Ridge adds a "penalty" term to the cost function equal to $\alpha \sum \theta_i^2$.

### Behavior
This forces the learning algorithm to not only fit the data but also keep the model weights as small as possible. Note that the bias term $\theta_0$ is usually not regularized.

### Usage
Use it whenever you suspect overfitting. $\alpha = 0$ is just Linear Regression; a very large $\alpha$ results in a flat line through the data's mean.
