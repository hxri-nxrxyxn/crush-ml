# ex107: Basic RNNs
### Processing Sequences
Unlike standard networks, RNNs have loops. They process data one step at a time, keeping a "memory" of previous steps. Ideal for time series and text.
### The State
At each step, the model takes the current input and the **hidden state** from the previous step.
