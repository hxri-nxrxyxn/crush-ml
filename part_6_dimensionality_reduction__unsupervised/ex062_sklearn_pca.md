# ex062: Scikit-Learn PCA

### Concept
Scikit-Learn’s `PCA` class uses SVD to project data onto a lower-dimensional space. It automatically takes care of centering the data for you.

### Benefits
- **Compression**: Reduces the size of the dataset significantly.
- **Visualization**: Reduces high-dimensional data (e.g., 100 features) to 2D or 3D so it can be plotted.
- **Noise Filtering**: By discarding the components with the lowest variance, you often discard noise.
