import os
import tarfile
import urllib.request

HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.tgz"

def download_data(housing_path=HOUSING_PATH, housing_url=HOUSING_URL):
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    tgz_file = tarfile.open(tgz_path)
    tgz_file.extractall(path=housing_path)
    tgz_file.close()

if __name__ == "__main__":
    download_data()
    print("housing data has been downloaded and extracted to:", HOUSING_PATH)
