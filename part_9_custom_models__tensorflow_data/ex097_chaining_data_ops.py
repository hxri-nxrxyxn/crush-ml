import tensorflow as tf
dataset = tf.data.Dataset.from_tensor_slices(tf.range(10))
dataset = dataset.repeat(3).batch(7)
print("Dataset operations chained: repeat(3), batch(7).")
for item in dataset.take(2):
    print(item.numpy())
