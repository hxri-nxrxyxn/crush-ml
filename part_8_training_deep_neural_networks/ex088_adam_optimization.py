from tensorflow import keras
optimizer = keras.optimizers.Adam(learning_rate=0.001, beta_1=0.9, beta_2=0.999)
print("Adam optimizer configured.")
