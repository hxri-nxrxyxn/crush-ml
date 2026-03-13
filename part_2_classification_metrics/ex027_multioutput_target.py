from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# Multioutput: each label can have multiple values (e.g. image denoising)
X = np.random.randint(0, 255, size=(100, 10)) # Noisy
y = np.random.randint(0, 255, size=(100, 10)) # Clean

knn_clf = KNeighborsClassifier()
knn_clf.fit(X, y)

print("Multioutput-multiclass classification (image denoising structure) trained.")
