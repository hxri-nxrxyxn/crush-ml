# ex044: Gaussian RBF Kernel

### Concept
The Radial Basis Function (RBF) kernel is the most common SVM kernel. It acts as if you added "similarity features" for every single point in the dataset.

### Hyperparameters
- **Gamma ($\gamma$)**: Controls the width of the bell-shaped curve. 
  - **Small $\gamma$**: A wide bell; points have a far-reaching influence (smooth boundary).
  - **Large $\gamma$**: A narrow bell; points have a very local influence (wiggly, complex boundary).
- **C**: General regularization (as seen in ex041).

### Strategy
Always try the RBF kernel if Linear SVM doesn't work. It is remarkably good at handling complex, non-linear boundaries.
