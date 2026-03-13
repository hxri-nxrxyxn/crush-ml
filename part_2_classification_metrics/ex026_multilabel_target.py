from sklearn.neighbors import KNeighborsClassifier
import numpy as np

X = np.random.randn(100, 10)
y_multilabel = np.random.randint(0, 2, size=(100, 2)) # Two binary labels

knn_clf = KNeighborsClassifier()
knn_clf.fit(X, y_multilabel)

print("KNeighborsClassifier trained for multilabel classification.")
print("Prediction for first instance:", knn_clf.predict([X[0]]))
