# ex064: Randomized PCA

### Concept
A stochastic algorithm that quickly finds an approximation of the first $d$ principal components.

### Performance
- **Time Complexity**: $O(m \times d^2) + O(d^3)$ instead of $O(m \times n^2) + O(n^3)$.
- **When to use**: When the dataset is large and you want to reduce it to a significantly smaller number of dimensions ($d \ll n$).
