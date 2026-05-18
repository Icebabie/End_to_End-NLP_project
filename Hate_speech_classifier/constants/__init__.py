import os
from datetime import datetime

# Common constants
TIMESTAMP: str = datetime.now().strftime("%d%m%Y_%H%M%S")
ARTIFACTS_DIR: str = os.path.join("artifacts", TIMESTAMP)
BUCKET_NAME: str = "hate_speech_icebabie"
ZIP_FILE_NAME: str = "dataset.zip"
LABEL = "label"
TWEET = "tweet"

# Data Ingestion constants
DATA_INGESTION_ARTIFACTS_DIR = "DataIngestionArtifacts"
DATA_INGESTION_IMBALANCE_DATA_DIR = "imbalanced_data.csv"
DATA_INGESTION_RAW_DATA_DIR = "raw_data.csv"
