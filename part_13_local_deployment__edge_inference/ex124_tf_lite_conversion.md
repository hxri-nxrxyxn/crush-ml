# ex124 & ex125: TensorFlow Lite and Quantization

### Concept (ex124)
TF Lite is designed for **Edge Devices** (mobile phones, IoT devices, microcontrollers). It converts a heavy model into a flatbuffer format that is extremely lightweight.

### Post-Training Quantization (ex125)
A technique to make models even smaller and faster.
- **How**: It converts 32-bit floating-point weights (FP32) into 8-bit integers (INT8).
- **Result**: The model size is reduced by 4x, and inference speed on CPUs increases significantly, with usually very little loss in accuracy.
