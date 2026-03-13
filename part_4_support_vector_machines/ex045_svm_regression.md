# ex045: SVM Regression

### Concept
SVM Regression reverses the objective of classification. 
- **Classification**: Fit the widest street between classes while limiting violations.
- **Regression**: Fit as many instances as possible **inside** the street while limiting violations (points outside the street).

### Characteristics
- **Epsilon ($\epsilon$)**: Controls the width of the street.
- **Insensitivity**: Adding more training instances inside the street doesn't affect the model’s predictions; hence, the model is "$\epsilon$-insensitive."

### Implementation
Use `LinearSVR` for linear regression and `SVR` for non-linear (kernelized) regression.
