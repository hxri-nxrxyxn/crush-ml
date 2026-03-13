# ex085: Transfer Learning

### Concept
Don't train from scratch! If you want to solve a new task, find an existing neural network that solves a similar task and reuse its lower layers.

### Strategy
1. Load the pre-trained model.
2. Replace the output layer with a new one for your task.
3. **Freeze** the reused layers (make them non-trainable) so their weights don't get destroyed during initial training.
4. Train the new head.
5. (Optional) **Fine-tune**: Unfreeze the lower layers and train again with a very low learning rate.
