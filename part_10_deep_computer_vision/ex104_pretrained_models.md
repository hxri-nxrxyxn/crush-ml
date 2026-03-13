# ex104: Using Pre-trained Models

### Concept
Instead of training your own CNN for weeks, use one that was trained by Google or Microsoft on the **ImageNet** dataset (1.4 million images).

### Popular Architectures in Keras
- **ResNet50**: Excellent all-rounder.
- **Xception**: Optimized for speed and accuracy.
- **MobileNet**: Tiny and fast, designed for phones.

### Usage
Set `weights="imagenet"`. If you want to use it for your own task, set `include_top=False` to remove the 1000-class output layer.
