# ex068: Silhouette Score

### Concept
Inertia is not a perfect metric because it keeps decreasing as you add more clusters. The **Silhouette Score** is a more precise way to find the "optimal" number of clusters.

### The Math
The silhouette coefficient for an instance is $(b - a) / max(a, b)$, where:
- $a$: Mean distance to other instances in the **same** cluster.
- $b$: Mean distance to instances in the **next closest** cluster.

### Interpretation
- **+1**: Instance is well inside its own cluster.
- **0**: Instance is on a cluster boundary.
- **-1**: Instance may have been assigned to the wrong cluster.
