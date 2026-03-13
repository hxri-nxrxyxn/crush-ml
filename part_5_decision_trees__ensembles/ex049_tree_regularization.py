from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_moons

X, y = make_moons(n_samples=100, noise=0.25, random_state=53)
# min_samples_leaf is a powerful regularization hyperparameter
tree_clf = DecisionTreeClassifier(min_samples_leaf=4, random_state=42)
tree_clf.fit(X, y)
print("Regularized Decision Tree trained with min_samples_leaf=4.")
