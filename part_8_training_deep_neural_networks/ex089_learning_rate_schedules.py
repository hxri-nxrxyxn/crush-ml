from tensorflow import keras
lr_schedule = keras.optimizers.schedules.ExponentialDecay(
    initial_learning_rate=0.01, decay_steps=10000, decay_rate=0.1)
optimizer = keras.optimizers.SGD(learning_rate=lr_schedule)
print("Exponential Learning Rate Schedule configured.")
