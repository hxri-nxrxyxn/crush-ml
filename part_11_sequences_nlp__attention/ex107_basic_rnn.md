# ex107 & ex108: Recurrent Neural Networks (RNNs)

### Concept
RNNs are designed to process **sequences** of data, such as time series or sentences. Unlike feedforward networks, they have "loops" that allow information to persist.

### How they work
At each time step $t$, the neuron receives the input $x_t$ AND its own output from the previous time step $h_{t-1}$. This forms a "memory."

### Deep RNNs (ex108)
You can stack multiple RNN layers. However, each layer (except the last) must return its full sequence of outputs (`return_sequences=True`) so the next layer has a sequence to process.
