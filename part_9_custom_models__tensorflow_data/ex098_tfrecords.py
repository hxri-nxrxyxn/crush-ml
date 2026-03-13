import tensorflow as tf
import os
filename = "my_test.tfrecord"
with tf.io.TFRecordWriter(filename) as writer:
    writer.write(b"Serialized data")
print("TFRecord file written:", os.path.exists(filename))
