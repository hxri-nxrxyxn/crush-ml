# ex073: Keras Sequential API

### Concept
The simplest way to build a neural network. It allows you to stack layers on top of each other in a linear sequence.

### Layers Breakdown
1. **Flatten**: Converts the input image (e.g., 28x28) into a 1D array (784 pixels). It has no parameters.
2. **Dense (Hidden)**: A fully connected layer. Each neuron computes a weighted sum of all inputs. We use **ReLU** (Rectified Linear Unit) as the activation function.
3. **Dense (Output)**: For multiclass classification (like Fashion MNIST), we use 10 neurons (one per class) with the **Softmax** activation function to get a probability distribution.
