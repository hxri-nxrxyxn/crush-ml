import pandas as pd
import os
from sklearn.preprocessing import OneHotEncoder

housing = pd.read_csv(os.path.join("datasets", "housing", "housing.csv"))
housing_cat = housing[["ocean_proximity"]]

cat_encoder = OneHotEncoder()
housing_cat_1hot = cat_encoder.fit_transform(housing_cat)
print("One-hot encoded shape:", housing_cat_1hot.shape)
print("Sparse matrix output (first row):\n", housing_cat_1hot[0])
