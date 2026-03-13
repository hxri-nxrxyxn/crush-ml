from tensorflow import keras
optimizer = keras.optimizers.SGD(learning_rate=0.001, momentum=0.9)
print("Momentum optimizer configured.")
