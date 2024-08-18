from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_validation import DataValiadtion
from mlProject import logger, CustomException
import sys



STAGE_NAME = "Data Validation stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config = data_validation_config)
        data_validation.validate_all_columns()
        data_validation.validate_missing_values()


if __name__ =='__main__':
    try:
        logger.info(f">>>>>>>>>> Stage {STAGE_NAME} Started <<<<<<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> Stage {STAGE_NAME} Completed <<<<<<<<<<")

    except Exception as e:
        raise CustomException(e,sys)
