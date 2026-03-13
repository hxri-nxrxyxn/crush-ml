# ex122: DCGAN (Deep Convolutional GAN)

### Concept
A GAN architecture that uses Convolutional layers instead of simple Dense layers.

### Key Guidelines (Radford et al.)
- Replace pooling layers with **strided convolutions** (in Discriminator) and **fractionally-strided convolutions** (in Generator).
- Use **Batch Normalization** in both networks.
- Use **ReLU** in the Generator and **LeakyReLU** in the Discriminator.
