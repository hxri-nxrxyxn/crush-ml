# ex030: Stochastic Gradient Descent (SGD)

### Concept
Instead of using the whole dataset, SGD picks a **random instance** in the training set at every step and computes the gradients based only on that single instance.

### Characteristics
- **Fast**: Can handle huge datasets since it only looks at one instance at a time.
- **Erratic**: The cost function will bounce up and down, decreasing only on average. It will never settle at the minimum but will end up very close.
- **Global Minima**: This randomness helps the algorithm jump out of local minima, making it better at finding the global minimum in complex non-convex functions than Batch GD.

### Learning Schedule
To make SGD settle down, we use a **Learning Schedule**—gradually reducing the learning rate as training progresses.
