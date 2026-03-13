# ex096 & ex097: TensorFlow Data API (tf.data)

### Concept
For large datasets that don't fit in RAM, you need a high-performance streaming API. `tf.data` is designed for this.

### Chaining Operations (ex097)
- **`repeat()`**: Loops through the dataset.
- **`shuffle(buffer_size)`**: Shuffles the data.
- **`batch(size)`**: Groups data into batches.
- **`map(fn)`**: Preprocesses the data in parallel.
- **`prefetch(1)`**: Prepares the next batch while the GPU is working on the current one (the most important for performance!).
