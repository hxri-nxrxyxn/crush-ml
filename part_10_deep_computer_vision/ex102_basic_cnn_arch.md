# ex102: Basic CNN Architecture

### Concept
A typical CNN architecture follows a standard pattern:
1. **Convolution + ReLU**
2. **Pooling**
3. **Convolution + ReLU**
4. **Pooling**
5. **Flatten**
6. **Dense (Fully Connected)**
7. **Softmax Output**

### Rule of Thumb
As you go deeper into the network, the image dimensions (width/height) should **decrease**, while the number of filters (depth) should **increase**.
