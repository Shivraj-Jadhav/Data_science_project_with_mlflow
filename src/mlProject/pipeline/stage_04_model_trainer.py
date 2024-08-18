from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_trainer import ModelTrainer
from mlProject import logger, CustomException
import sys



STAGE_NAME = "Model Trainer stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer_config = ModelTrainer(config=model_trainer_config)
            model_trainer_config.train()

        except Exception as e:
            raise CustomException(e,sys)


if __name__ =='__main__':
    try:
        logger.info(f">>>>>>>>>> Stage {STAGE_NAME} Started <<<<<<<<<<")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> Stage {STAGE_NAME} Completed <<<<<<<<<<")

    except Exception as e:
        raise CustomException(e,sys)
