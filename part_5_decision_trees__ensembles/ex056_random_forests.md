# ex056: Random Forests

### Concept
A Random Forest is an ensemble of Decision Trees, generally trained via the bagging method.

### Added Randomness
Instead of searching for the very best feature when splitting a node, Random Forests search for the best feature among a **random subset of features**. This results in even greater tree diversity, which trades a higher bias for a lower variance, yielding a better overall model.

### ExtraTrees
If you use random thresholds for each feature instead of searching for the best possible thresholds, you get an **Extremely Randomized Tree** ensemble (Extra-Trees).
