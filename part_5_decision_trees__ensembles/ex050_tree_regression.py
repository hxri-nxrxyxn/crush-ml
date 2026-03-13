from sklearn.tree import DecisionTreeRegressor
import numpy as np

X = np.random.rand(100, 1)
y = 4 * (X - 0.5) ** 2 + np.random.randn(100, 1) / 10

tree_reg = DecisionTreeRegressor(max_depth=2, random_state=42)
tree_reg.fit(X, y)
print("Decision Tree Regressor trained. Prediction for [0.6]:", tree_reg.predict([[0.6]]))
