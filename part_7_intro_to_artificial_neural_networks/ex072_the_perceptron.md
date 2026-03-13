# ex072: The Perceptron

### Concept
The Perceptron is one of the simplest ANN architectures, based on a **threshold logic unit (TLU)**. It computes a weighted sum of its inputs plus a bias, then applies a step function.

### Formula
$$h_w(x) = step(w^T x + b)$$

### Training (Hebb’s Rule)
Perceptrons are trained using a variant of Gradient Descent. If a neuron makes a mistake, it reinforces the connections from inputs that would have contributed to the correct prediction.

### Limitation
Perceptrons can only solve **linearly separable** problems. They famously failed to solve the XOR (exclusive OR) problem, leading to the "AI Winter" until Multi-Layer Perceptrons (MLPs) were developed.
