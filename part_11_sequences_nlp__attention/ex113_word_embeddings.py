from tensorflow import keras
embedding = keras.layers.Embedding(input_dim=1000, output_dim=50)
print("Word Embedding layer defined (Vocab size 1000, Output dim 50).")
