# ex101: Max Pooling

### Concept
Pooling layers are used to **subsample** (shrink) the input image. 

### Why use Pooling?
- **Reduces Parameters**: Shrinking the image reduces the number of computations in the next layers.
- **Invariance**: It makes the model slightly "invariant" to small translations (shifting the object a few pixels doesn't change the max value in the pooling window).

### How it works
Max Pooling looks at a window (e.g., 2x2) and only keeps the **maximum** value.
