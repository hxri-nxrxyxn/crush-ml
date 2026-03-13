# ex109 & ex110: LSTMs and GRUs

### The Problem with Basic RNNs
Standard RNNs have a very short-term memory. Due to the vanishing gradient problem, information from early in a sequence is lost by the time the network reaches the end.

### LSTM (Long Short-Term Memory)
LSTMs use a complex architecture with "gates" (forget, input, and output gates) to control the flow of information. This allows them to remember information for hundreds of time steps.

### GRU (Gated Recurrent Unit)
A simplified version of the LSTM. It merges the cell state and hidden state and uses fewer gates. It is often faster to train and performs almost as well as LSTMs.
