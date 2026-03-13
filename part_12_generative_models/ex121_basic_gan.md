# ex121: Generative Adversarial Networks (GANs)

### Concept
GANs are composed of two neural networks that play a game against each other.

### The Players
1. **Generator**: Tries to create fake data that looks real (the "art forger").
2. **Discriminator**: Tries to distinguish between real data and fake data (the "art critic").

### Training (Minimax)
During training, the Generator gets better at fooling the Discriminator, and the Discriminator gets better at catching the fakes. Eventually, the Generator produces data indistinguishable from reality.
