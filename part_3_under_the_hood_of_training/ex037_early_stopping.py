from sklearn.base import clone
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import mean_squared_error
import numpy as np

# Mocking data and best model search
X_train = np.random.rand(100, 1)
y_train = (4 + 3 * X_train + np.random.randn(100, 1)).ravel()

sgd_reg = SGDRegressor(max_iter=1, tol=None, warm_start=True,
                       penalty=None, learning_rate="constant", eta0=0.0005, random_state=42)

minimum_val_error = float("inf")
best_epoch = None
best_model = None
for epoch in range(100):
    sgd_reg.fit(X_train, y_train)
    y_val_predict = sgd_reg.predict(X_train) # Using train as mock validation
    val_error = mean_squared_error(y_train, y_val_predict)
    if val_error < minimum_val_error:
        minimum_val_error = val_error
        best_epoch = epoch
        best_model = clone(sgd_reg)

print("Early stopping best epoch found:", best_epoch)
