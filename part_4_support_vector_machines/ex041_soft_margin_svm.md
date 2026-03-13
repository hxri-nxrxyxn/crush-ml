# ex041: Soft Margin SVM (Tuning C)

### Concept
The hyperparameter `C` controls the balance between two goals:
1. Keeping the street as wide as possible.
2. Limiting margin violations.

### Tuning C
- **Small C**: Leads to a wider street but more violations (High bias, Low variance). Better for preventing overfitting.
- **Large C**: Leads to a narrower street but fewer violations (Low bias, High variance). Use if the model is underfitting.

### Implementation Tip
In Scikit-Learn, `LinearSVC` is faster than `SVC(kernel="linear")` because it is optimized specifically for the linear case.
