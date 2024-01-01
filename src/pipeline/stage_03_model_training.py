from src.components.model_training import Training
from src.configuration import ConfigurationManager
from src.logger import logging


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


if __name__ == "__main__":
    try:
        logging.info(">>> Model Training Component Started.")
        model_trainer = ModelTrainingPipeline()
        model_trainer.main()
        logging.info(">>> Model Training Component Ended.")

    except Exception as e:
        raise e
