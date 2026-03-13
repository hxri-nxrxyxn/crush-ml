# ex008: Handling Missing Values
### Three Strategies
1. **Drop rows**: `dropna()`. Fine if you have millions of rows.
2. **Drop columns**: `drop()`. Use if the feature is useless.
3. **Impute (Fill)**: `fillna(median)`. The professional choice.
### The Median Rule
Always compute the median on the **training set only**. Use that same value later for the test set and production data.
