# ex100: 2D Convolution Layers

### Concept
Convolutional layers are the building blocks of Computer Vision. Unlike dense layers that look for patterns anywhere, Conv layers look for **local patterns** (edges, textures) using small filters (kernels).

### Key Terms
- **Filters (Kernels)**: Small matrices (e.g., 3x3) that slide over the image to create a "feature map."
- **Padding**: Adding zeros around the image to ensure the output has the same dimensions as the input (`padding="same"`).
- **Strides**: The step size of the filter. A stride of 2 halves the output dimensions.
