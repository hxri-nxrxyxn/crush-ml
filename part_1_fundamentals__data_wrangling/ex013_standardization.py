from sklearn.preprocessing import StandardScaler
import numpy as np

data = np.array([[1], [2], [3], [4], [5]])
scaler = StandardScaler()
scaled = scaler.fit_transform(data)
print("Standardized data (Mean 0, Std 1):\n", scaled.flatten())
