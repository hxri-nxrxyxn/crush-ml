# ex074: Compiling Keras Models

### Concept
Before training, you must specify the loss function, the optimizer, and the metrics.

### Key Parameters
- **Loss**: Use `sparse_categorical_crossentropy` when you have multiple classes and the targets are integers (0, 1, 2...). Use `categorical_crossentropy` if targets are one-hot encoded.
- **Optimizer**: `sgd` (Stochastic Gradient Descent) is the classic choice. Keras will perform the backpropagation for you.
- **Metrics**: `accuracy` is the most common for classification.
