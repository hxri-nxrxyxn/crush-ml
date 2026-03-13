# ex081: Weight Initialization (Glorot and He)

### The Problem
If the weights in a neural network start out too large, the activations will explode. If they start out too small, the signal will vanish before reaching the final layers.

### Solutions
Researchers found that for the signal to flow properly, we need the variance of the outputs of each layer to be equal to the variance of its inputs.

1. **Glorot (Xavier) Initialization**: Designed for layers using Logistic, Tanh, or Softmax activations.
2. **He Initialization**: Specifically designed for layers using the **ReLU** activation function and its variants.

### Implementation
In Keras, the default is Glorot. To use He, specify `kernel_initializer="he_normal"`.
