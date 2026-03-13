from tensorflow import keras
optimizer = keras.optimizers.SGD(clipvalue=1.0)
print("Optimizer with Gradient Clipping (clipvalue=1.0) configured.")
