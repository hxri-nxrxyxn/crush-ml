# ex024: Multiclass Classification (OvR vs OvO)

### Concept
Some algorithms (like Logistic Regression or Random Forests) handle multiple classes natively. Others (like SVMs) are strictly binary.

### Two Strategies
1. **One-versus-the-Rest (OvR)**: Train 10 binary classifiers (one for each digit). To classify an image, get the score from all 10 and pick the highest. (Preferred for most models).
2. **One-versus-One (OvO)**: Train a classifier for every pair of digits (0 vs 1, 0 vs 2, etc.). For $N$ classes, you need $N(N-1)/2$ classifiers. (Preferred for SVMs because they scale poorly with dataset size).

### Scikit-Learn
Scikit-Learn detects when you try to use a binary algorithm for a multiclass task and automatically runs OvR (or OvO for SVMs).
