import os
from pathlib import Path
from dotenv import dotenv_values
from src.utils import read_yaml, create_directories
from src.config_entity import (
    DataIngestionConfig,
    PrepareBaseModelConfig,
    TrainingConfig,
    EvaluationConfig,
)

config = dotenv_values(".env")

DATA_SOURCE_URL = config["DATA_SOURCE_URL"]
FILE_NAME: str = config["FILE_NAME"]
MLFLOW_TRACKING_URI: str = config["MLFLOW_TRACKING_URI"]

CONFIG_FILE_PATH: str = Path("config/config.yaml")
PARAMS_FILE_PATH: str = Path("params.yaml")


class ConfigurationManager:
    def __init__(
        self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH
    ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        return DataIngestionConfig(
            root_dir=config.root_dir,
            data_source_URL=DATA_SOURCE_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir,
        )

    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model

        create_directories([config.root_dir])

        return PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_class=self.params.CLASS,
        )

    def get_training_config(self) -> TrainingConfig:
        training = self.config.training
        prepare_base_model = self.config.prepare_base_model
        params = self.params
        training_data = os.path.join(self.config.data_ingestion.unzip_dir, FILE_NAME)
        create_directories([Path(training.root_dir)])

        return TrainingConfig(
            root_dir=Path(training.root_dir),
            trained_model_path=Path(training.trained_model_path),
            updated_base_model_path=Path(prepare_base_model.updated_base_model_path),
            training_data=Path(training_data),
            params_epochs=params.EPOCHS,
            params_batch_size=params.BATCH_SIZE,
            params_is_augmentation=params.AUGMENTATION,
            params_image_size=params.IMAGE_SIZE,
        )

    def get_evaluation_config(self) -> EvaluationConfig:
        return EvaluationConfig(
            path_of_model=Path(self.config.training.trained_model_path),
            training_data=Path(
                os.path.join(self.config.data_ingestion.unzip_dir, FILE_NAME)
            ),
            mlflow_uri=MLFLOW_TRACKING_URI,
            all_params=self.params,
            params_image_size=self.params.IMAGE_SIZE,
            params_batch_size=self.params.BATCH_SIZE,
        )
