# ex075: Training and the History Object

### Concept
When you call `model.fit()`, it returns a **History** object.

### Contents
- `history.params`: Training parameters (epochs, steps).
- `history.epoch`: List of epochs run.
- `history.history`: A dictionary containing the loss and extra metrics measured at the end of each epoch on both the training set and the validation set.

### Usage
This is vital for plotting learning curves. If you see the training accuracy going up while validation accuracy goes down, your model is **overfitting**.
