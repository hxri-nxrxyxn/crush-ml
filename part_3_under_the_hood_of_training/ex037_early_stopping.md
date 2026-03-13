# ex037: Early Stopping

### Concept
A completely different way to regularize iterative learning algorithms (like Gradient Descent). You stop training as soon as the validation error reaches a minimum.

### Why it works
As training continues, the model learns the noise in the training set, causing the validation error to start going back up. Géron calls early stopping a "beautiful free lunch."
