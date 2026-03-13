# ex103: ResNet and Skip Connections

### The Problem
In very deep networks (100+ layers), the signal can vanish during backpropagation, making training impossible.

### The Solution: Residual Learning
Introduce **Skip Connections** (or shortcuts). The signal from an earlier layer is added directly to the output of a later layer.
$$Output = F(x) + x$$

### Why it works
If the network is already optimal, it can simply set the weights of the hidden layers to zero ($F(x)=0$), and the signal will just pass through ($Output = x$). This makes deep networks much easier to train.
