# ex028: The Normal Equation
### Math vs Iteration
The Normal Equation is a direct formula to find the best weights: theta = (X'X)^-1 X'y.
### Pros
Perfect solution in one step. No learning rate needed.
### Cons
Very slow if you have many features (O(n^3)). Requires lots of RAM.
