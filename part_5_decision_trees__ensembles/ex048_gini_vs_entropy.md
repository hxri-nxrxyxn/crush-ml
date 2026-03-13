# ex048: Gini Impurity vs. Entropy

### Gini Impurity
$$G_i = 1 - \sum_{k=1}^n p_{i,k}^2$$
A node is "pure" ($G=0$) if all training instances it applies to belong to the same class.

### Entropy
In ML, entropy is used as an impurity measure. A set’s entropy is zero when it contains instances of only one class.
$$H_i = -\sum_{k=1}^n p_{i,k} \log_2(p_{i,k})$$

### Which one to use?
- **Gini**: Default. Slightly faster to compute. It tends to isolate the most frequent class in its own branch.
- **Entropy**: Tends to produce slightly more balanced trees.
- **Verdict**: Most of the time it doesn't make a big difference.
