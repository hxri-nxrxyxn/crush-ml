# ex051 & ex052: Voting Classifiers (Hard vs Soft)

### Concept
A "Wisdom of the Crowd" approach. You train several different classifiers (Logistic, SVM, Random Forest) and aggregate their predictions. Even if each individual is a "weak learner," the ensemble can be a "strong learner."

### Hard Voting
The ensemble predicts the class that got the **majority of votes** from the individual classifiers.

### Soft Voting
The ensemble predicts the class with the **highest average probability**. 
- **Requirement**: All classifiers must be able to estimate class probabilities (`predict_proba()`).
- **Performance**: Usually works better than hard voting because it gives more weight to highly confident votes.
