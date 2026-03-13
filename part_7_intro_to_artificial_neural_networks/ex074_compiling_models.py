import tensorflow as tf
from tensorflow import keras

model = keras.models.Sequential([keras.layers.Dense(10, input_shape=[5])])
model.compile(loss="sparse_categorical_crossentropy",
              optimizer="sgd",
              metrics=["accuracy"])
print("Keras model compiled with SGD optimizer.")
