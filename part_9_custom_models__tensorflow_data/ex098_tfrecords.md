# ex098: TFRecord Format

### Concept
The TFRecord format is TensorFlow's own binary format for storing large amounts of data efficiently. 

### Structure
It stores a sequence of binary strings. Usually, each string is a serialized `Example` protocol buffer, containing one or more features (images, labels, etc.).

### Use Case
Use TFRecords when you have massive datasets (terabytes) or want to speed up data loading in distributed training environments.
