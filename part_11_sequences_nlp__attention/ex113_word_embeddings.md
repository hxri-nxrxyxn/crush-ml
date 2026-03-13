# ex113: Word Embeddings

### Concept
Computers don't understand words. One-hot encoding is inefficient ($100,000+$ dimensions for a full vocabulary). **Embeddings** map each word to a dense vector of fixed size (e.g., 50 or 300).

### Semantic Relationship
During training, the model places words with similar meanings (e.g., "King" and "Queen") close to each other in this multidimensional space.
