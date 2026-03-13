import tensorflow as tf
from tensorflow import keras

class MyExponentialLayer(keras.layers.Layer):
    def call(self, inputs):
        return tf.exp(inputs)

model = keras.models.Sequential([
    keras.layers.Dense(10, input_shape=[5]),
    MyExponentialLayer()
])
print("Model with custom exponential activation layer built.")
