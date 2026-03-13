# PREREQUISITE: YOU MUST RUN ex001_fetching_data.py FIRST TO DOWNLOAD THE DATASET.
import pandas as pd
import os

housing = pd.read_csv(os.path.join("datasets", "housing", "housing.csv"))
# Filter for numeric columns for correlation
corr_matrix = housing.select_dtypes(include=['number']).corr()
print("Correlations with Median House Value:")
print(corr_matrix["median_house_value"].sort_values(ascending=False))
