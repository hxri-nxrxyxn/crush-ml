# ex112: Character-level RNN (Char-RNN)

### Concept
Instead of processing words, the model processes one character at a time. 

### Shakespeare Example
In the book, Géron uses a Char-RNN to generate text in the style of Shakespeare. By learning the probability of the next character (e.g., given "th", what is the probability of "e"?), the model eventually learns to spell words and even structure dialogue.
