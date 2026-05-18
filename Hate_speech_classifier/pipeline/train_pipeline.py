import sys
from Hate_speech_classifier.logger import logging
from Hate_speech_classifier.exception import CustomException
from Hate_speech_classifier.components.data_ingestion import DataIngestion
from Hate_speech_classifier.entity.config_entity import (DataIngestionConfig)
from Hate_speech_classifier.entity.artifact_entity import (DataIngestionArtifact)

class TrainPipeline:
  def __init__(self):
    self.data_ingestion_config = DataIngestionConfig()
    

  def start_data_ingestion(self) -> DataIngestionArtifact:
    logging.info("Starting the data ingestion process in the training pipeline.")
    try:
      logging.info("Getting the data from Google Cloud Storage bucket.")
      data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)

      data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()
      logging.info("Data ingestion process completed successfully.")
      logging.info("Exited the data ingestion process in the training pipeline.")
      return data_ingestion_artifacts
    
    except Exception as e:
      raise CustomException(e, sys) from e
    

  def run_pipeline(self):
    logging.info("Starting the training pipeline.")
    try:
      data_ingestion_artifacts = self.start_data_ingestion()
      


      logging.info("Training pipeline completed successfully.")

    except Exception as e:
      raise CustomException(e, sys) from e