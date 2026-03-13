# ex027: Multioutput Classification

### Concept
A generalization of multilabel classification where each label can be multiclass (i.e., it can have more than two possible values).

### Image Denoising Example
- **Input**: A noisy image of a digit (784 pixels).
- **Target**: The original clean image (784 labels).
- **Label Value**: Each pixel is a label, and its value can range from 0 to 255.

This model predicts 784 different values simultaneously to "clean" the input.
