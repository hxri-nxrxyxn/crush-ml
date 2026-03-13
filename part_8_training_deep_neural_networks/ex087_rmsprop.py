from tensorflow import keras
optimizer = keras.optimizers.RMSprop(learning_rate=0.001, rho=0.9)
print("RMSProp optimizer configured.")
