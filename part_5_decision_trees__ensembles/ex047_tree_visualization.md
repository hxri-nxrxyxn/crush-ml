# ex047: Tree Visualization

### Concept
One of the best features of Decision Trees is that they are easy to interpret. You can visualize the decision-making process as a flow chart.

### Components of a Node
- **Samples**: How many training instances it applies to.
- **Value**: How many training instances of each class this node applies to.
- **Class**: The predicted class for that node.
- **Gini**: The node's impurity (0 means the node is perfectly pure).

### Implementation
Use `export_graphviz` to generate a `.dot` file, which can be converted to an image using Graphviz.
