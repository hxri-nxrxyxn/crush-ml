from sklearn.ensemble import GradientBoostingRegressor
import numpy as np

X = np.random.rand(100, 1)
y = 3*X**2 + 0.05*np.random.randn(100, 1)

gbrt = GradientBoostingRegressor(max_depth=2, n_estimators=3, learning_rate=1.0, random_state=42)
gbrt.fit(X, y.ravel())
print("Gradient Boosting Regressor trained.")
