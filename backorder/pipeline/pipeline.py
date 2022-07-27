from backorder.config.configuration import Configuartion
from backorder.logger import logging
from backorder.exception import BackorderPredictionException

from backorder.entity.artifact_entity import DataIngestionArtifact
from backorder.entity.config_entity import DataIngestionConfig
from backorder.component.data_ingestion import DataIngestion
import os,sys

class Pipeline:

    def __init__(self, config: Configuartion = Configuartion()) -> None:
        try:
            self.config = config

        except Exception as e:
            raise BackorderPredictionException(e, sys) from e

    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise BackorderPredictionException(e, sys) from e    


    def start_data_validation(self):
        pass

    def start_data_transformation(self):
        pass

    def start_model_trainer(self):
        pass

    def start_model_evaluation(self):
        pass

    def start_model_pusher(self):
        pass

    def run_pipeline(self):
        try:
            #data ingestion

            data_ingestion_artifact = self.start_data_ingestion()

        except Exception as e:
            raise BackorderPredictionException(e,sys) from e