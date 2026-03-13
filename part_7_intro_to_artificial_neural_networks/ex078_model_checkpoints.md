# ex078: Callbacks: Model Checkpoints

### Concept
Training can take hours or days. If your computer crashes, you lose everything. 

### Implementation
The `ModelCheckpoint` callback saves your model at regular intervals during training.
- **`save_best_only=True`**: This ensures that you only keep the version of the model that performed best on the validation set, protecting you from overfitting.
