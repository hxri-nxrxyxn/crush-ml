from tensorflow import keras
layer = keras.layers.Dense(100, activation="elu",
                           kernel_initializer="he_normal",
                           kernel_regularizer=keras.regularizers.l2(0.01))
print("Dense layer with L2 regularization (0.01) created.")
