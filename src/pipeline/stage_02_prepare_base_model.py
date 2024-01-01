from src.components.prepare_base_model import PrepareBaseModel
from src.configuration import ConfigurationManager
from src.logger import logging


class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()


if __name__ == "__main__":
    try:
        logging.info(">>> Prepare Base Model Component Started.")
        prepare_base_model = PrepareBaseModelTrainingPipeline()
        prepare_base_model.main()
        logging.info(">>> Prepare Base Model Component Ended.")

    except Exception as e:
        raise e
