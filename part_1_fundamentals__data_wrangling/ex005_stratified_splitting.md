# ex005: Stratified Splitting
### Solving Sampling Bias
If you sample 1,000 people and don't ensure gender balance, your survey is biased. In ML, we must ensure the test set represents the whole population.
### Median Income Strata
Since income is the most important predictor, we create income categories (strata) and ensure the test set has the same income proportions as the training set using `StratifiedShuffleSplit`.
