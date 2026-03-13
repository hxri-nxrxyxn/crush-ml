# PREREQUISITE: YOU MUST RUN ex001_fetching_data.py FIRST TO DOWNLOAD THE DATASET.
import os
import pandas as pd
import matplotlib.pyplot as plt

housing = pd.read_csv(os.path.join("datasets", "housing", "housing.csv"))
housing.hist(bins=50, figsize=(20,15))
print("Histograms generated. Median income bin counts:")
print(housing["median_income"].value_counts(bins=5))
