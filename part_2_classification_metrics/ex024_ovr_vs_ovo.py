from sklearn.multiclass import OneVsOneClassifier
from sklearn.linear_model import SGDClassifier
import numpy as np

X = np.random.randn(100, 10)
y = np.random.randint(0, 3, size=100) # 3 classes

# SGD uses OvR by default. Forcing OvO:
ovo_clf = OneVsOneClassifier(SGDClassifier(random_state=42))
ovo_clf.fit(X, y)

print("OneVsOneClassifier trained on 3 classes.")
print("Number of estimators:", len(ovo_clf.estimators_))
