import tensorflow as tf
X = tf.range(10)
dataset = tf.data.Dataset.from_tensor_slices(X)
print("tf.data.Dataset created from range(10):")
for item in dataset.take(3):
    print(item.numpy())
