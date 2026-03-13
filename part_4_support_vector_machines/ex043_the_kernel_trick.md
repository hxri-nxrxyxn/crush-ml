# ex043: The Kernel Trick

### Concept
A mathematical miracle that allows you to get the same result as if you had added many polynomial features, but **without actually adding them**. 

### Why it works
The optimization problem for SVMs only depends on the **dot product** of the training instances. The "Kernel Trick" replaces this dot product with a "Kernel Function" that represents the dot product in a higher-dimensional space.

### Implementation
Use the `SVC` class with `kernel="poly"`. The hyperparameter `coef0` controls how much the model is influenced by high-degree versus low-degree polynomials.
