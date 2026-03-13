# ex002: Exploratory Data Analysis (EDA)
### Taking a Quick Look
Before math, comes understanding. We use **Pandas** to perform a "vibe check" on our data.
1. **head()**: Shows the first 5 rows. Check for column names and basic value ranges.
2. **info()**: Critical for finding **missing values (NaNs)**. Note that `total_bedrooms` has fewer non-null values than other columns.
3. **describe()**: Shows statistics. Note the percentiles (25, 50, 75). The 50th percentile is the **Median**.
