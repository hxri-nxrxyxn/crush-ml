# ex093 & ex094: Custom Layers

### Stateless Layers (ex093)
If you just want a layer that performs a fixed operation (like `tf.exp()` or `tf.square()`), you can use `keras.layers.Lambda` or inherit from `Layer` and only implement `call()`.

### Stateful Layers (ex094)
If you want a layer with its own weights, you inherit from `Layer` and implement:
1. **`__init__`**: Save hyperparameters.
2. **`build()`**: Create the weights (variables).
3. **`call()`**: The actual computation.
