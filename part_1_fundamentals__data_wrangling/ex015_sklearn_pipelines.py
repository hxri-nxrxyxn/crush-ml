# PREREQUISITE: YOU MUST RUN ex001_fetching_data.py FIRST TO DOWNLOAD THE DATASET.
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

num_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy="median")),
        ('std_scaler', StandardScaler()),
    ])

print("Sequential Pipeline defined with Imputer and Scaler.")
