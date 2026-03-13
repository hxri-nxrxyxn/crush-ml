# ex024: Multiclass Strategies
1. **One-vs-Rest (OvR)**: Train 10 detectors (0-detector, 1-detector, etc.). Pick the highest score.
2. **One-vs-One (OvO)**: Train a detector for every pair (0 vs 1, etc.).
Scikit-Learn handles this automatically under the hood.
