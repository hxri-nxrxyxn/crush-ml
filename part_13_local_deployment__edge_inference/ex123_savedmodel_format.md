# ex123: The SavedModel Format

### Concept
When you are ready to put a TensorFlow model into production, you should save it in the **SavedModel** format.

### Benefits
- **Architecture + Weights**: It saves the actual computation graph, including the weights and custom layers.
- **Language Neutral**: You can load a SavedModel in C++, Java, or Go, even if you trained it in Python.
- **Serving**: It is the required format for high-performance serving tools like **TensorFlow Serving**.
