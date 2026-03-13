# ex023: The ROC Curve and AUC

### Concept
The Receiver Operating Characteristic (ROC) curve plots the **True Positive Rate (Recall)** against the **False Positive Rate (FPR)**.
$$FPR = 1 - Specificity$$

### AUC (Area Under the Curve)
- **1.0**: Perfect classifier.
- **0.5**: Random guessing (diagonal line).

### PR vs ROC
- Use **PR** if the positive class is rare or you care about False Positives.
- Use **ROC** if you care about the overall performance across all threshold settings.
