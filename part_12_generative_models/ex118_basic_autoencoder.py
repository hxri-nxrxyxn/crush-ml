from tensorflow import keras
encoder = keras.models.Sequential([keras.layers.Flatten(input_shape=[28, 28]), keras.layers.Dense(30)])
decoder = keras.models.Sequential([keras.layers.Dense(28 * 28, input_shape=[30]), keras.layers.Reshape([28, 28])])
autoencoder = keras.models.Sequential([encoder, decoder])
print("Basic Linear Autoencoder built.")
