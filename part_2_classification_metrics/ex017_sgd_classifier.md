# ex017: SGD Classifier (Binary Classification)

### Concept
The Stochastic Gradient Descent (SGD) classifier is a simple yet powerful algorithm capable of handling very large datasets efficiently. This is because it deals with training instances one at a time.

### Implementation Notes
- **Dataset**: MNIST (70,000 images of handwritten digits).
- **Target**: We simplify the problem into a "binary" task: Is the digit a 5? (True/False).
- **Randomness**: SGD relies on randomness during training. If you want reproducible results, you must set `random_state`.

### Theory
SGD is particularly well-suited for **online learning**, where the model is updated as new data arrives.
