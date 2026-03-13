import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.linear_model import SGDClassifier

mnist = fetch_openml('mnist_784', version=1, as_frame=False)
X, y = mnist["data"], mnist["target"].astype(np.uint8)
X_train, y_train = X[:60000], y[:60000]
y_train_5 = (y_train == 5)

sgd_clf = SGDClassifier(random_state=42)
sgd_clf.fit(X_train, y_train_5)
print("SGD Classifier trained for binary classification (Is '5').")
print("Prediction for first instance:", sgd_clf.predict([X[0]]))
