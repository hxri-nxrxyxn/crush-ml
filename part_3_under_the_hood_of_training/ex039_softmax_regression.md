# ex039: Softmax Regression

### Concept
Also known as Multinomial Logistic Regression. It generalizes Logistic Regression to support multiple classes directly, without having to train multiple binary classifiers.

### How it works
1. Computes a score $s_k(x)$ for each class $k$.
2. Estimates the probability of each class using the **Softmax Function** (normalized exponential).
3. Predicts the class with the highest probability.

### Constraint
It can only predict one class at a time (classes must be mutually exclusive). For example, it can predict "Apple" or "Orange," but not both at once.
