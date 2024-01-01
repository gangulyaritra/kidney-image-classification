from src.components.model_evaluation import Evaluation
from src.configuration import ConfigurationManager
from src.logger import logging


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
        logging.info(">>> Model Evaluation Component Started.")
        model_evaluation = EvaluationPipeline()
        model_evaluation.main()
        logging.info(">>> Model Evaluation Component Ended.")

    except Exception as e:
        raise e
