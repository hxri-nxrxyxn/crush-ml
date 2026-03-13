# ex077: Subclassing API

### Concept
For researchers who need absolute control. You create a class that inherits from `keras.Model`.

### Structure
1. **`__init__`**: Define the layers you want to use.
2. **`call()`**: Define the computations (the forward pass).

### Pros and Cons
- **Pros**: Dynamic behavior. You can use loops, if-statements, and other custom Python logic inside the forward pass.
- **Cons**: Your model architecture is hidden inside Python code, making it harder for Keras to inspect, save, or clone.
