from tensorflow import keras
denoising_encoder = keras.models.Sequential([
    keras.layers.Flatten(input_shape=[28, 28]),
    keras.layers.GaussianNoise(0.1),
    keras.layers.Dense(30)
])
print("Denoising Autoencoder (with Gaussian Noise) built.")
