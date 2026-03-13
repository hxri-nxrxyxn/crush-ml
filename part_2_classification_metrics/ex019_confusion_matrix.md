# ex019: Confusion Matrix

### Concept
The confusion matrix is the ultimate tool for evaluating classification. It shows exactly how many times instances of class A were classified as class B.

### The Matrix Layout
- **Row**: Actual class.
- **Column**: Predicted class.

| | Predicted Negative | Predicted Positive |
| :--- | :--- | :--- |
| **Actual Negative** | **True Negative (TN)** | False Positive (FP) |
| **Actual Positive** | False Negative (FN) | **True Positive (TP)** |

### Key takeaway
A perfect classifier would only have non-zero values on its main diagonal (TN and TP).
