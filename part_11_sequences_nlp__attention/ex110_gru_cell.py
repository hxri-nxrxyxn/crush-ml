from tensorflow import keras
model = keras.models.Sequential([
    keras.layers.GRU(20, return_sequences=True, input_shape=[None, 1]),
    keras.layers.GRU(20),
    keras.layers.Dense(1)
])
print("GRU (Gated Recurrent Unit) model built.")
