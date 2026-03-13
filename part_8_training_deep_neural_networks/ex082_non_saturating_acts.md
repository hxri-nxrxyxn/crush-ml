# ex082: Non-Saturating Activation Functions

### The Problem with Sigmoid
The Logistic (Sigmoid) function saturates for high or low values (the slope becomes almost zero). This means the gradient is tiny, and backpropagation effectively stops. This is the **Vanishing Gradients** problem.

### The Alternatives
1. **ReLU**: Rectified Linear Unit. Fast and doesn't saturate for positive values.
2. **LeakyReLU**: $max(\alpha z, z)$. Prevents neurons from "dying" (outputting zero forever) by giving them a small slope for negative values.
3. **ELU / SELU**: Exponential Linear Unit. Often outperform ReLU but are slower to compute. SELU allows the network to "self-normalize," keeping the mean and variance constant across layers.
