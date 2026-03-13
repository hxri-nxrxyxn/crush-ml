# PREREQUISITE: YOU MUST RUN ex001_fetching_data.py FIRST TO DOWNLOAD THE DATASET.
import pandas as pd
import os
from pandas.plotting import scatter_matrix

housing = pd.read_csv(os.path.join("datasets", "housing", "housing.csv"))
attributes = ["median_house_value", "median_income", "total_rooms", "housing_median_age"]
print("Attributes selected for scatter matrix:", attributes)
# In a script, we verify correlations instead of plotting
print(housing[attributes].corr())
