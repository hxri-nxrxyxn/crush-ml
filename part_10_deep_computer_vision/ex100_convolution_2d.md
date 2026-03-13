# ex100: 2D Convolution Layers
### The Eye of the Model
Conv layers use small filters (kernels) to scan images for patterns.
- **Edges**: Early layers find simple lines.
- **Shapes**: Middle layers find circles or squares.
- **Objects**: Final layers recognize complex objects like eyes or wheels.
### Parameters
- **Padding="same"**: Keeps output size the same as input.
- **Strides**: Step size of the scan.
