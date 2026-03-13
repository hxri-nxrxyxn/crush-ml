# ex103: ResNet and Skip Connections
### The Vanishing Problem
In extremely deep networks, the gradient disappears before reaching the first layers.
### Skip Connections
Residual Units add the input directly to the output: `H(x) = F(x) + x`. This allows the signal to "skip" layers, making it possible to train networks with hundreds of layers.
