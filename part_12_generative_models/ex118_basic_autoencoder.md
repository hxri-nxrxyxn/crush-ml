# ex118: Basic Autoencoders

### Concept
Autoencoders are neural networks capable of learning dense representations of the input data (called **codings**) without any supervision.

### Architecture
1. **Encoder (Recognition Network)**: Converts the input to an internal representation.
2. **Decoder (Generative Network)**: Converts the internal representation back to the original format.

### The Bottleneck
The hidden layer (the codings) must have a smaller dimension than the input. This forces the autoencoder to learn the most important features and discard the noise.
