from src.components.data_ingestion import DataIngestion
from src.components.prepare_base_model import PrepareBaseModel
from src.components.model_training import Training
from src.components.model_evaluation import Evaluation
from src.configuration import ConfigurationManager
from src.logger import logging


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        evaluation_config = config.get_evaluation_config()
        evaluation = Evaluation(evaluation_config)
        evaluation.evaluation()
        evaluation.save_score()
        evaluation.log_into_mlflow()


if __name__ == "__main__":
    try:
        logging.info(">>> Data Ingestion Component Started.")
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()
        logging.info(">>> Data Ingestion Component Ended.")

    except Exception as e:
        raise e

    try:
        logging.info(">>> Prepare Base Model Component Started.")
        prepare_base_model = PrepareBaseModelTrainingPipeline()
        prepare_base_model.main()
        logging.info(">>> Prepare Base Model Component Ended.")

    except Exception as e:
        raise e

    try:
        logging.info(">>> Model Training Component Started.")
        model_trainer = ModelTrainingPipeline()
        model_trainer.main()
        logging.info(">>> Model Training Component Ended.")

    except Exception as e:
        raise e

    try:
        logging.info(">>> Model Evaluation Component Started.")
        model_evaluation = EvaluationPipeline()
        model_evaluation.main()
        logging.info(">>> Model Evaluation Component Ended.")

    except Exception as e:
        raise e
