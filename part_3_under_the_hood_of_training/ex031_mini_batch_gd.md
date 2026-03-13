# ex031: Mini-batch Gradient Descent

### Concept
A middle ground between Batch and Stochastic GD. It computes the gradients on small random sets of instances called **mini-batches**.

### Advantage
You can get a performance boost from hardware optimization of matrix operations, especially when using GPUs. It is less erratic than SGD but faster than Batch GD.

### Comparison Table
| Algorithm | Dataset Size | Out-of-core support | Scaling ($n$) | Settle at Min? |
| :--- | :--- | :--- | :--- | :--- |
| **Normal Eq** | Small | No | Slow | Yes |
| **Batch GD** | Large | No | Fast | Yes |
| **Stochastic GD**| Huge | Yes | Fast | No |
| **Mini-batch GD**| Huge | Yes | Fast | No |
