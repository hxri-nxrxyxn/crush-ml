# ex042: Polynomial SVM

### Concept
If your data is not linearly separable, one approach is to add polynomial features (like $x^2$, $x^3$, etc.). This often makes the data separable in a higher-dimensional space.

### Moons Example
In the book, Géron uses the "moons" dataset. By adding polynomial features up to degree 3, a linear SVM can easily find a non-linear boundary that separates the two crescent shapes.

### Limitation
Adding actual polynomial features can make the feature set explode if the degree is high, making the model incredibly slow.
