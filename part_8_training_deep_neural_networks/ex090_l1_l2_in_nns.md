# ex090 & ex091: Regularization (L1/L2 and Dropout)

### L1 and L2 (ex090)
Just like in linear models, you can apply L2 regularization to Keras layers to keep weights small, or L1 to create a sparse model.

### Dropout (ex091)
The most popular regularization technique for Deep Learning.
- **How it works**: At every training step, every neuron (except output neurons) has a probability $p$ (e.g., 20%) of being temporarily "dropped out" (ignored).
- **Why it works**: A neuron cannot rely on its neighbors to do the work; it must be as useful as possible on its own. This forces the network to learn more robust features.
- **Inference**: Dropout is only active during training.
