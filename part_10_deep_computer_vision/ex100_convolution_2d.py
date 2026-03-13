from tensorflow import keras
conv = keras.layers.Conv2D(filters=32, kernel_size=3, padding="same", activation="relu", input_shape=[28, 28, 1])
print("Conv2D layer defined with 32 filters, 3x3 kernel.")
