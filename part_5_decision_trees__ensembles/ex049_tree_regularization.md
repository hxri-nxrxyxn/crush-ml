# ex049: Tree Regularization

### The Problem
Decision Trees are **non-parametric**: they don't have a fixed number of parameters. If left unconstrained, the tree will adapt itself to every tiny noise in the training data, leading to extreme **overfitting**.

### Regularization Hyperparameters
- **`max_depth`**: Limits the number of levels.
- **`min_samples_split`**: Minimum samples a node must have before it can be split.
- **`min_samples_leaf`**: Minimum samples a leaf node must have. (Very effective!)
- **`max_leaf_nodes`**: Maximum number of leaf nodes.

### Strategy
Always constrain the tree. Increasing `min_*` hyperparameters or decreasing `max_*` hyperparameters will regularize the model.
