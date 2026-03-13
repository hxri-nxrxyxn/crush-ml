# ex084: Gradient Clipping

### Concept
Specifically useful for **Recurrent Neural Networks (RNNs)** where Batch Normalization is hard to use. 

### Implementation
Instead of letting gradients grow indefinitely, we "clip" them so that they never exceed a certain threshold (e.g., 1.0). This prevents the optimization from diverging due to exploding gradients.
