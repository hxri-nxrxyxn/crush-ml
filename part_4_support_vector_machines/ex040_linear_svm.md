# ex040: Linear SVM Classification

### Concept
Support Vector Machines (SVMs) try to fit the widest possible "street" (the gap between classes) between the data points. This is called **Large Margin Classification**.

### Characteristics
- **Support Vectors**: The points that fall on the edge of the "street." Adding more points far away from the boundary doesn't change the model at all.
- **Scaling**: SVMs are extremely sensitive to feature scales. If features aren't scaled (e.g., age vs. income), the model will ignore the smaller scale features.

### Hard Margin vs Soft Margin
- **Hard Margin**: Only works if data is linearly separable and has no outliers.
- **Soft Margin**: Allows some "margin violations" (points on the street or even the wrong side) to achieve a better generalization.
