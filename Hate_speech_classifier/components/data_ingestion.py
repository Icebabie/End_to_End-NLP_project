import os
import sys
from zipfile import ZipFile
from Hate_speech_classifier.logger import logging
from Hate_speech_classifier.exception import CustomException
from Hate_speech_classifier.configuration.gcloud_syncer import GcloudSync
from Hate_speech_classifier.entity.config_entity import DataIngestionConfig
from Hate_speech_classifier.entity.artifact_entity import DataIngestionArtifact


class DataIngestion:
  def __init__(self, data_ingestion_config : DataIngestionConfig):
    self.data_ingestion_config = data_ingestion_config
    self.gcloud_sync = GcloudSync()

  def get_data_from_gcloud(self) -> None:
    try:
      logging.info("Starting data ingestion from Google Cloud Storage.")
      os.makedirs(self.data_ingestion_config.DATA_INGESTION_ARTIFACTS_DIR, exist_ok=True)
      self.gcloud_sync.sync_folder_from_gcloud(self.data_ingestion_config.BUCKET_NAME,
                                              self.data_ingestion_config.ZIP_FILE_NAME,
                                              self.data_ingestion_config.DATA_INGESTION_ARTIFACTS_DIR)
      logging.info("exited from gcloud syncer")

    except Exception as e:
      raise CustomException(e, sys) from e
    
  def unzip_and_save(self):
    try:
      logging.info("Starting to unzip the downloaded dataset.")

      with ZipFile(self.data_ingestion_config.ZIP_FILE_PATH, 'r') as zip_ref:
        zip_ref.extractall(self.data_ingestion_config.ZIP_FILE_DIR)

      logging.info("Dataset unzipped successfully.")
      return self.data_ingestion_config.DATA_ARTIFACTS_DIR, self.data_ingestion_config.NEW_DATA_ARTIFACTS_DIR
    except Exception as e:
      raise CustomException(e, sys) from e
    
  def initiate_data_ingestion(self) -> DataIngestionArtifact:
    try:
      logging.info("Initiating data ingestion process.")
      self.get_data_from_gcloud()
      logging.info("Fetched the dataset from Google Cloud Storage successfully.")
      imbalance_data_file_path, raw_data_file_path = self.unzip_and_save()
      logging.info("Data ingestion process completed successfully.")

      data_ingestion_artifacts = DataIngestionArtifact(
        imbalance_data_file_path=imbalance_data_file_path,
        raw_data_file_path=raw_data_file_path
      )

      logging.info("Exited from data ingestion method.")
      logging.info(f"Data Ingestion Artifact: {data_ingestion_artifacts}")

    except Exception as e:
      raise CustomException(e, sys) from e