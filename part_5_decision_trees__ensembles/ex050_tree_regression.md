# ex050: Decision Tree Regression

### Concept
Instead of predicting a class, each node in a regression tree predicts a **value**. This value is simply the **average target value** of the training instances associated with that leaf node.

### Optimization
Instead of minimizing impurity (Gini), the CART algorithm splits the data in a way that minimizes the **Mean Squared Error (MSE)**.

### Warning
Regression trees are very sensitive to outliers and, just like classification trees, will overfit if not regularized.
