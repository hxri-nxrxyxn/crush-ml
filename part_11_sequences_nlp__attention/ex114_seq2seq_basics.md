# ex114: Seq2Seq (Encoder-Decoder)

### Concept
Used for tasks where the input and output are both sequences of different lengths (e.g., Machine Translation).

### Architecture
1. **Encoder**: Processes the input sequence (English) and compresses it into a final state vector.
2. **Decoder**: Takes that state vector and starts generating the output sequence (French) one word at a time.
