from sklearn.tree import export_text
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()
tree_clf = DecisionTreeClassifier(max_depth=2, random_state=42)
tree_clf.fit(iris.data, iris.target)

tree_rules = export_text(tree_clf, feature_names=iris['feature_names'])
print("Decision Tree structure (text representation):\n", tree_rules)
