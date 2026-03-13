# ex035: Lasso Regression (L1 Regularization)

### Concept
Least Absolute Shrinkage and Selection Operator (Lasso). It adds a penalty equal to $\alpha \sum |\theta_i|$.

### Key Difference from Ridge
Lasso tends to completely eliminate the weights of the least important features (sets them to zero). 

### Result
Lasso automatically performs **feature selection** and outputs a **sparse model** (a model with few non-zero weights).
