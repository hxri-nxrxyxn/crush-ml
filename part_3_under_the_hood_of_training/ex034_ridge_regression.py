from sklearn.linear_model import Ridge
import numpy as np

X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

ridge_reg = Ridge(alpha=1, solver="cholesky", random_state=42)
ridge_reg.fit(X, y)
print("Ridge Regression Intercept/Coef:", ridge_reg.intercept_, ridge_reg.coef_)
