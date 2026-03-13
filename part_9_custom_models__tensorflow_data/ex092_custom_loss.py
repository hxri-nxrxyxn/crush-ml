import tensorflow as tf
from tensorflow import keras

def huber_fn(y_true, y_pred):
    error = y_true - y_pred
    is_small_error = tf.abs(error) < 1
    return tf.where(is_small_error, tf.square(error)/2, tf.abs(error)-0.5)

model = keras.models.Sequential([keras.layers.Dense(1, input_shape=[10])])
model.compile(loss=huber_fn, optimizer="sgd")
print("Model compiled with custom Huber loss function.")
