# ex115: The Attention Mechanism

### The Problem with Seq2Seq
The "bottleneck": the entire meaning of a long sentence must be squeezed into a single fixed-size vector.

### The Solution: Attention
Instead of looking only at the final encoder state, the Decoder "pays attention" to the most relevant parts of the **entire input sequence** at each step of the translation.
