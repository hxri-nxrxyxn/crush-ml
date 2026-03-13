# ex105 & ex106: Localization and Segmentation

### Object Localization (ex105)
Predicting where an object is in the image. You add a **regression head** to your CNN that outputs 4 values: $[x, y, width, height]$.

### Semantic Segmentation (ex106)
Predicting the class of **every single pixel** in the image.
- **FCN (Fully Convolutional Network)**: A CNN with no dense layers. 
- **Upsampling**: We use `Conv2DTranspose` to "blow up" the small feature maps back to the original image size.
