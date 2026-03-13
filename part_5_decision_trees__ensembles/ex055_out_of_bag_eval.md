# ex055: Out-of-Bag (OOB) Evaluation

### Concept
In Bagging, some instances are sampled several times for any given predictor, while others are not sampled at all. 

### The Math
On average, only about **63%** of the training instances are sampled for each predictor. The remaining 37% are called **Out-of-Bag (OOB)** instances.

### Benefit
Since the model never saw these OOB instances during training, you can use them for validation **without needing a separate validation set**. This allows you to use your entire dataset for training while still having a reliable evaluation metric.
