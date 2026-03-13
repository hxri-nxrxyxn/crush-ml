# ex111: 1D Convolutions for Sequences

### Concept
If you have a very long sequence (like an audio waveform), RNNs can be too slow. A **1D Convolutional Layer** can slide a filter across the temporal dimension to extract features.

### Benefit
Conv1D layers are much faster than RNNs because they can process segments of the sequence in parallel. They are often used as a preprocessing step before an RNN.
