from sklearn.preprocessing import MinMaxScaler
import numpy as np

data = np.array([[1], [2], [3], [4], [5]])
scaler = MinMaxScaler()
scaled = scaler.fit_transform(data)
print("Min-Max scaled data [1-5]:\n", scaled.flatten())
