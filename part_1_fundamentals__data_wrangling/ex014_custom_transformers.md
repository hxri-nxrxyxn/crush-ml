# ex014: Custom Transformers
### Cleaning Code
By wrapping your logic (like adding `rooms_per_household`) in a class, you can plug it into a Scikit-Learn Pipeline.
### Requirements
Inherit from `BaseEstimator` and `TransformerMixin`. Implement `fit()` and `transform()`.
