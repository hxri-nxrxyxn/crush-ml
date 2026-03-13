# ex127: Headless Optimization

### Concept
In production environments (like a Docker container on a server), you often want to restrict the number of CPU threads used by NumPy or TensorFlow to prevent them from "fighting" for resources.

### Implementation
Use environment variables like `OMP_NUM_THREADS` and `TF_NUM_INTRAOP_THREADS` to force the model to use a specific number of cores.
