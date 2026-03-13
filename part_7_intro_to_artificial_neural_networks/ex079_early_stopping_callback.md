# ex079: Callbacks: Early Stopping

### Concept
Training for too many epochs leads to overfitting. Training for too few leads to underfitting. 

### Implementation
The `EarlyStopping` callback monitors the validation loss. If the loss doesn't improve for a certain number of epochs (defined by `patience`), it automatically stops the training and restores the best weights.
