from tensorflow import keras
model = keras.models.Sequential([
    keras.layers.Conv1D(filters=20, kernel_size=4, strides=2, padding="valid", input_shape=[None, 1]),
    keras.layers.GRU(20),
    keras.layers.Dense(1)
])
print("1D Convolutional layer for sequence processing built.")
