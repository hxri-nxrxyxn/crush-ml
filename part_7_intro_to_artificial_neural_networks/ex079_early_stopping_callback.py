import tensorflow as tf
from tensorflow import keras
early_stopping_cb = keras.callbacks.EarlyStopping(patience=10, restore_best_weights=True)
print("EarlyStopping callback initialized.")
