# ex032: Polynomial Regression

### Concept
What if your data is more complex than a straight line? You can still use a linear model to fit non-linear data. 

### Strategy
Add powers of each feature as new features. 
*Example:* If you have one feature $x$, you can add $x^2$ as a second feature. The model is still linear in its parameters ($\theta$), even though it fits a curve.

### Implementation
Use Scikit-Learn’s `PolynomialFeatures`. Be careful: high degrees (e.g., degree 100) will likely lead to **overfitting**.
