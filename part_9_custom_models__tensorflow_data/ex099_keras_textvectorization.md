# ex099: Keras Preprocessing Layers

### Concept
You can now include data preprocessing (like text vectorization or image augmentation) directly **inside your model**.

### Benefits
- **Portability**: When you export the model, the preprocessing logic goes with it. You don't need a separate script to clean text before sending it to the API.
- **Speed**: These layers are optimized and can run on the GPU.
