from tensorflow import keras
# LeakyReLU, ELU, SELU
model = keras.models.Sequential([
    keras.layers.Dense(10, kernel_initializer="he_normal"),
    keras.layers.LeakyReLU(alpha=0.2),
    keras.layers.Dense(10, activation="elu")
])
print("Model with non-saturating activations (LeakyReLU, ELU) built.")
