from tensorflow import keras
model = keras.models.Sequential([
    keras.layers.Dropout(rate=0.2),
    keras.layers.Dense(300, activation="elu", kernel_initializer="he_normal"),
    keras.layers.Dense(10, activation="softmax")
])
print("Model with Dropout (rate=0.2) built.")
