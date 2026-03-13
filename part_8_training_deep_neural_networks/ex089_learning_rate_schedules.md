# ex089: Learning Rate Scheduling

### Concept
Finding the perfect learning rate is hard. Instead of a constant rate, we change it over time.

### Strategies
1. **Power Scheduling**: Drops the rate slower and slower.
2. **Exponential Scheduling**: Drops the rate by a factor of 10 every $S$ steps. (Preferred for its simplicity).
3. **Performance Scheduling**: Drop the rate when the validation error stops decreasing (ReduceLROnPlateau).
4. **1cycle Scheduling**: Starts by increasing the LR, then drops it back down. Often leads to much faster training.
