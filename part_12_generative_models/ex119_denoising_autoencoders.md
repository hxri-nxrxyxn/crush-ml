# ex119: Denoising Autoencoders

### Concept
Instead of just compressing data, we train the autoencoder to remove noise.

### How it works
1. Add random noise to the input images (or use Dropout).
2. The target for the autoencoder is the **original clean image**.
3. The model must learn the underlying structure of the data to "guess" what the clean version looked like.

### Usage
This is a powerful way to perform **unsupervised pre-training** or to clean up corrupted signals.
