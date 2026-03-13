import tensorflow as tf
from tensorflow import keras
import numpy as np

X = np.random.rand(100, 28, 28)
y = np.random.randint(0, 10, size=100)

model = keras.models.Sequential([
    keras.layers.Flatten(input_shape=[28, 28]),
    keras.layers.Dense(10, activation="softmax")
])
model.compile(loss="sparse_categorical_crossentropy", optimizer="sgd", metrics=["accuracy"])

import matplotlib.pyplot as plt
import pandas as pd

history = model.fit(X, y, epochs=10, verbose=0)
print("Training History Keys:", history.history.keys())

pd.DataFrame(history.history).plot(figsize=(8, 5))
plt.grid(True)
plt.gca().set_ylim(0, 5) # Setting range for visual clarity
plt.title("Learning Curves (Loss and Accuracy)")
plt.show()
