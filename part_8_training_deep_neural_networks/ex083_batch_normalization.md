# ex083: Batch Normalization (BN)

### Concept
BN adds an operation in the model just before or after the activation function of each hidden layer. It zero-centers and normalizes each input, then scales and shifts the result.

### Benefits
- **Eliminates Vanishing Gradients**: Makes the model much more robust to poor initialization.
- **Faster Convergence**: You can use much larger learning rates.
- **Regularization**: Acts like a light regularizer, reducing the need for other techniques like Dropout.

### Downside
BN adds complexity to the model and slightly slows down predictions because of the extra computations required.
