import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Set the KAGGLE_CONFIG_DIR environment variable to the directory containing your kaggle.json
os.environ['KAGGLE_CONFIG_DIR'] = r'C:\Users\Mostafa Magdy\Documents\Summer Course\Adv. AI\myenv\kaggle api'

print("KAGGLE_CONFIG_DIR:", os.environ.get('KAGGLE_CONFIG_DIR'))

# Initialize Kaggle API
api = KaggleApi()
api.authenticate()

# Define the dataset identifier (e.g., 'waqi786/dogs-dataset-3000-records')
# dataset_identifier = 'waqi786/dogs-dataset-3000-records'
dataset_identifier = 'emineyetm/fake-news-detection-datasets'
print(f"Attempting to download dataset: {dataset_identifier}")

# Download the dataset
api.dataset_download_files(dataset_identifier, path='datasets', unzip=True)
print("Dataset downloaded and unzipped in the 'datasets' directory.")
