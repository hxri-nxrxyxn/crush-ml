from tensorflow import keras
layer = keras.layers.Dense(10, activation="relu", kernel_initializer="he_normal")
print("Dense layer with He initialization created.")
