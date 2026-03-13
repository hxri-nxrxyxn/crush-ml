# PREREQUISITE: YOU MUST RUN ex001_fetching_data.py FIRST TO DOWNLOAD THE DATASET.
import pandas as pd
import os
from sklearn.model_selection import train_test_split

housing = pd.read_csv(os.path.join("datasets", "housing", "housing.csv"))
train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)

print(f"Train size: {len(train_set)}, Test size: {len(test_set)}")
