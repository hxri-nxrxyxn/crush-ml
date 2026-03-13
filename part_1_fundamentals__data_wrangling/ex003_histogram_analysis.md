# ex003: Histogram Analysis
### Visualizing Distributions
Histograms show the number of instances for each value range.
### Critical Observations
1. **Capping**: `median_house_value` is capped at $500,000. Your model might never learn to predict higher values unless you remove these capped districts.
2. **Tail Heaviness**: Many features are "skewed" to the right. ML models prefer bell-shaped (Normal) distributions.
3. **Scaling**: Features have wildly different ranges (0-15 vs 0-500,000). We will need to scale these later.
