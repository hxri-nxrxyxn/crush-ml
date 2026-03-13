# ex073: Keras Sequential API

### Concept
The Sequential API is the easiest way to build a neural network. You just stack layers like LEGO bricks.

### Layer Types
1.  **`Flatten`**: This doesn't "learn" anything. It just reshapes the input. If you give it a 28x28 image, it squashes it into a 1D array of 784 pixels.
2.  **`Dense`**: This is a "Fully Connected" layer. Every neuron in this layer is connected to every neuron in the previous layer.
3.  **Activation (ReLU)**: We use the Rectified Linear Unit ($max(0, z)$). It's fast and helps the model learn complex patterns.

### Fashion MNIST
Instead of handwritten digits, we use 70,000 images of clothing (T-shirts, trousers, sneakers). It's a much harder problem than the original MNIST!
---
# ex074: Compiling the Model

### Concept
Before you start training, you have to tell Keras how to measure its performance and how to improve.

### Three Key Ingredients
1.  **Loss Function**: How "wrong" the model is.
    - `sparse_categorical_crossentropy`: Use this when you have multiple classes (0-9) and they are mutually exclusive.
2.  **Optimizer**: The algorithm that tweaks the weights.
    - `sgd`: Stochastic Gradient Descent. It's the classic method of moving "downhill" toward lower error.
3.  **Metrics**: What you want to track.
    - `accuracy`: The percentage of images correctly classified.
---
# ex075: The History Object

### Concept
When you call `model.fit()`, Keras returns a **History** object. This is a goldmine of information!

### What's inside?
It contains a dictionary with the loss and accuracy measured at the end of every epoch. 
- **Training curves**: Show how the model is learning the training data.
- **Validation curves**: Show how the model performs on data it hasn't seen yet.

### Analyzing Learning Curves
- If the curves are close together, your model is generalizing well.
- If the training error is much lower than the validation error, your model is **overfitting** (memorizing the training set instead of learning the patterns).
---
# ex076: Keras Functional API

### Concept: Wide & Deep
Not all models are simple stacks. The **Wide & Deep** architecture allows the model to learn both simple rules (the Wide path) and complex patterns (the Deep path).

### Why use it?
A regular MLP forces all data to flow through all layers, which can distort simple signals. By connecting some inputs directly to the output, the model can "memorize" obvious rules while "generalizing" complex ones.

### Multiple Inputs
The Functional API allows you to send different features to different paths. For example, you might send "Location" to the Wide path and "Age/Income" to the Deep path.
---
# ex077: Subclassing API

### Concept
For ultimate flexibility, you can build a model as a Python class. 

### Structure
1.  **`__init__`**: You create the layers here.
2.  **`call()`**: You define the math. You can even use `if` statements and loops!

### When to use it
Researchers use this when they are inventing entirely new types of networks that don't fit into the standard "stack" or "graph" patterns of Keras.
---
# ex078 & ex079: Callbacks (Checkpoints & Early Stopping)

### Model Checkpoints (ex078)
If your computer crashes during a 10-hour training session, you lose all progress. The `ModelCheckpoint` callback saves your model's weights to disk after every epoch.
- **`save_best_only=True`**: This only saves the model if it outperformed its previous best score on the validation set.

### Early Stopping (ex079)
Why train for 100 epochs if the model stops improving after 20? 
- `EarlyStopping` monitors the validation loss and "pulls the plug" as soon as the model stops getting better. This is a "beautiful free lunch" that prevents overfitting and saves time.
---
# ex080: TensorBoard

### Concept
TensorBoard is a powerful visualization tool. It allows you to:
1.  Watch your accuracy and loss curves live in your web browser.
2.  Visualize the actual "graph" (architecture) of your neural network.
3.  Analyze the weights and biases of every layer.

### Implementation
Simply create a log directory and pass the `TensorBoard` callback to your `model.fit()` call.
