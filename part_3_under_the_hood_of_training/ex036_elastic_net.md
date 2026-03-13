# ex036: Elastic Net

### Concept
A middle ground between Ridge and Lasso. It is a weighted mix of both their penalty terms.
- **Mix ratio ($r$)**: When $r=0$, it's Ridge. When $r=1$, it's Lasso.

### When to use
- Ridge is the default.
- If you suspect only a few features are useful, use Lasso or Elastic Net.
- Elastic Net is preferred over Lasso when features are highly correlated or when the number of features is greater than the number of instances.
