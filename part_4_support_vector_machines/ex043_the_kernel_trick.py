from sklearn.svm import SVC
from sklearn.datasets import make_moons

X, y = make_moons(n_samples=100, noise=0.15, random_state=42)

poly_kernel_svm_clf = SVC(kernel="poly", degree=3, coef0=1, C=5)
poly_kernel_svm_clf.fit(X, y)
print("SVM with Polynomial Kernel Trick trained.")
