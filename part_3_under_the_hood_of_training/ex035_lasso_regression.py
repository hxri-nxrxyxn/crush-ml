from sklearn.linear_model import Lasso
import numpy as np

X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

lasso_reg = Lasso(alpha=0.1)
lasso_reg.fit(X, y)
print("Lasso Regression Intercept/Coef:", lasso_reg.intercept_, lasso_reg.coef_)
