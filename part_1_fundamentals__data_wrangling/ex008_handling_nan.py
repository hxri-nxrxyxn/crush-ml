import pandas as pd
import os

housing = pd.read_csv(os.path.join("datasets", "housing", "housing.csv"))
# Option 3 from book: fill with median
median = housing["total_bedrooms"].median()
housing["total_bedrooms"].fillna(median, inplace=True)
print("NaNs filled with median in 'total_bedrooms':", median)
print("Remaining NaNs:", housing["total_bedrooms"].isnull().sum())
