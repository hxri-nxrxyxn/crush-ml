# ex004: Random Splitting
### The Golden Rule
**Never look at your test set.** If you do, you'll fall into **Data Snooping Bias**, picking a model that works on the test set by chance but fails in the real world.
### Concept
We reserve 20% of data for the "final exam." We use `random_state=42` to ensure the split is reproducible. Without a seed, you'd eventually see the whole dataset across multiple runs.
