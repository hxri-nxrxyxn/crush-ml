import tensorflow as tf
from tensorflow import keras
checkpoint_cb = keras.callbacks.ModelCheckpoint("my_keras_model.keras", save_best_only=True)
print("ModelCheckpoint callback initialized.")
