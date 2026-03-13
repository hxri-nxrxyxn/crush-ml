# PREREQUISITE: YOU MUST RUN ex001_fetching_data.py FIRST TO DOWNLOAD THE DATASET.
import pandas as pd
import os
from sklearn.preprocessing import OrdinalEncoder

housing = pd.read_csv(os.path.join("datasets", "housing", "housing.csv"))
housing_cat = housing[["ocean_proximity"]]

ordinal_encoder = OrdinalEncoder()
housing_cat_encoded = ordinal_encoder.fit_transform(housing_cat)
print("First 5 encoded values:", housing_cat_encoded[:5].flatten())
print("Categories:", ordinal_encoder.categories_)
