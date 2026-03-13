# ex028: The Normal Equation

### Mathematical Concept
The Normal Equation is a closed-form solution to find the value of $\theta$ that minimizes the cost function (MSE) directly.
$$\hat{\theta} = (X^T X)^{-1} X^T y$$

### Computation Complexity
- **Time Complexity**: Computing $(X^T X)^{-1}$ is roughly $O(n^{2.4})$ to $O(n^3)$ where $n$ is the number of features.
- **Scaling**: If you double the number of features, the computation time increases by roughly $2^{2.4} \approx 5.3$ to $2^3 = 8$ times.
- **Instances**: It handles large numbers of training instances ($m$) efficiently, as it is linear $O(m)$.

### When to use
Use it when you have a small number of features (e.g., under 10,000). For massive feature sets, use Gradient Descent.
