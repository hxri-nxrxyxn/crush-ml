# ex058: AdaBoost (Adaptive Boosting)

### Concept
Boosting refers to any ensemble method that can combine several weak learners into a strong learner by training them **sequentially**.

### How AdaBoost works
1. Train a base classifier (usually a Decision Stump—a tree with depth 1).
2. Increase the weight of training instances that the classifier misclassified.
3. Train a second classifier using the updated weights.
4. Repeat.

### Result
The ensemble "focuses" more and more on the difficult cases. It’s like a student learning from their mistakes on previous exams.
