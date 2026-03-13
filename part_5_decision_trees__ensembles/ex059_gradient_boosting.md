# ex059: Gradient Boosting (GBRT)

### Concept
Like AdaBoost, Gradient Boosting trains learners sequentially. However, instead of updating weights, it tries to fit the new predictor to the **residual errors** made by the previous predictor.

### Formula
$$Model_{new}(x) = Model_{old}(x) + Predictor_{error}(x)$$

### Learning Rate (Shrinkage)
If you set a low learning rate, you will need more trees in the ensemble, but the predictions will usually generalize better.
