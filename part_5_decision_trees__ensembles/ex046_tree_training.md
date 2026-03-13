# ex046: Decision Tree Training

### Concept
Decision Trees are versatile algorithms that can perform both classification and regression. They are the fundamental building blocks of Random Forests.

### Training (CART Algorithm)
Scikit-Learn uses the **Classification and Regression Tree (CART)** algorithm. 
1. It splits the training set into two subsets using a single feature $k$ and a threshold $t_k$. 
2. It searches for the pair $(k, t_k)$ that produces the "purest" subsets (weighted by their size).
3. It repeats this recursively until it reaches the maximum depth or cannot find a split that reduces impurity.

### Characteristics
- **White Box**: Decision Trees are "white box" models; you can easily visualize and understand their logic (see ex047).
- **No Scaling**: Unlike SVMs, Decision Trees require **no feature scaling** or centering at all.
