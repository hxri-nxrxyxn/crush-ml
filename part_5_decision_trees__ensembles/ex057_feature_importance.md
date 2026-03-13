# ex057: Feature Importance

### Concept
Random Forests make it very easy to measure the relative importance of each feature. 

### How it's measured
Scikit-Learn looks at how much the tree nodes that use that feature reduce impurity on average (across all trees in the forest). 

### Usage
This is an incredibly useful tool for **feature selection**. You can train a quick Random Forest to figure out which variables are actually doing the work before moving to a more complex model.
