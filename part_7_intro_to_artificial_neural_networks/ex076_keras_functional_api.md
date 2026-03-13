# ex076: Keras Functional API (Wide & Deep)

### Concept
Not all neural networks are simple stacks. The Functional API allows for complex topologies with multiple inputs or multiple outputs.

### Wide & Deep Learning
A famous architecture by Heng-Tze Cheng. 
- **Wide path**: Connects all or part of the inputs directly to the output layer. This allows the model to learn simple, shallow rules (memorization).
- **Deep path**: Passes inputs through a stack of hidden layers. This allows the model to learn complex patterns (generalization).

### Implementation
You define the layers as functions: `hidden1 = Dense(30, activation="relu")(input_layer)`.
