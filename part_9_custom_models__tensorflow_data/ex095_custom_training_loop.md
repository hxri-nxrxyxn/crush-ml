# ex095: Custom Training Loop

### Concept
`model.fit()` is easy, but it’s a "black box." A custom training loop gives you absolute control over how gradients are computed and applied.

### How it works
1. **`tf.GradientTape()`**: Records operations for automatic differentiation.
2. **`tape.gradient()`**: Computes the gradient of the loss with respect to the weights.
3. **`optimizer.apply_gradients()`**: Updates the weights using the computed gradients.

### When to use
Use this for advanced research projects, Generative Adversarial Networks (GANs), or complex architectures where different parts of the model need different optimization steps.
