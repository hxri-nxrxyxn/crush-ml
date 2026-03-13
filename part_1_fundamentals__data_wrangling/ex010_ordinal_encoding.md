# ex010: Ordinal Encoding
### Mapping Text to Numbers
Converts categories like "Poor", "Good" to 0, 1.
### The Trap
Only use this for **ordered** data. For "Ocean Proximity", the model might think category 0 is "less than" category 1, which is geographically meaningless.
