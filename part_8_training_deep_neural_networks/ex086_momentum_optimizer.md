# ex086, ex087, ex088: Advanced Optimizers

### Momentum Optimization (ex086)
Imagine a bowling ball rolling down a gentle slope: it will start slowly but quickly gather momentum. It uses the gradient as acceleration, not as speed. This helps skip over local minima and navigate flat regions.

### RMSProp (ex087)
Root Mean Square Propagation. It scales down the adaptive learning rate for dimensions that have large gradients, helping the optimizer focus on the "steepest" direction.

### Adam Optimization (ex088)
Adaptive Moment Estimation. It combines the ideas of **Momentum** and **RMSProp**. It tracks both the exponentially decaying average of past gradients and past squared gradients. It is currently the most popular "go-to" optimizer.
