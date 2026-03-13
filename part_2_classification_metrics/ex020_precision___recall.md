# ex020: Precision, Recall, and F1 Score

### Precision
The accuracy of the positive predictions.
$$Precision = \frac{TP}{TP + FP}$$
*Question it answers:* "Of all digits predicted as 5, what percentage were actually 5?"

### Recall (Sensitivity)
The ratio of positive instances that are correctly detected by the classifier.
$$Recall = \frac{TP}{TP + FN}$$
*Question it answers:* "Of all the actual 5s in the dataset, what percentage did the model find?"

### F1 Score
The harmonic mean of precision and recall. It gives much more weight to low values.
$$F_1 = \frac{2}{\frac{1}{precision} + \frac{1}{recall}}$$
The F1 score is high only if **both** precision and recall are high.
