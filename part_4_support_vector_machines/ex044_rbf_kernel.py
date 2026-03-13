from sklearn.svm import SVC
from sklearn.datasets import make_moons

X, y = make_moons(n_samples=100, noise=0.15, random_state=42)

rbf_kernel_svm_clf = SVC(kernel="rbf", gamma=5, C=0.001)
rbf_kernel_svm_clf.fit(X, y)
print("SVM with RBF Kernel Trick trained.")
