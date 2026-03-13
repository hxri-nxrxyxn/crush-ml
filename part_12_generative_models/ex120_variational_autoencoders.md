# ex120: Variational Autoencoders (VAEs)

### Concept
Unlike basic autoencoders, VAEs are **generative**. They don't just compress an image; they learn the **probability distribution** of the training data.

### The Math
Instead of outputting a fixed coding vector, the encoder outputs a **mean** ($\mu$) and a **standard deviation** ($\sigma$). A random sample is then taken from this Gaussian distribution and passed to the decoder.

### Result
You can generate entirely new, realistic data points (like new faces or digits) by sampling from the latent space.
