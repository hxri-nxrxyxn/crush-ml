# PREREQUISITE: YOU MUST RUN ex001_fetching_data.py FIRST TO DOWNLOAD THE DATASET.
import pandas as pd
import os
from sklearn.impute import SimpleImputer

housing = pd.read_csv(os.path.join("datasets", "housing", "housing.csv"))
housing_num = housing.drop("ocean_proximity", axis=1)

imputer = SimpleImputer(strategy="median")
imputer.fit(housing_num)
X = imputer.transform(housing_num)

housing_tr = pd.DataFrame(X, columns=housing_num.columns, index=housing.index)
print("Imputer statistics (medians):", imputer.statistics_)
print("Transformed data shape:", housing_tr.shape)
