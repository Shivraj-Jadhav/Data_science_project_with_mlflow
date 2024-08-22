from mlProject import logger, CustomException
import sys
import os
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03_data_tansformation import DataTransformationTrainingPipeline
from mlProject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from mlProject.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
logger.info("Welcome to the Project.\n\n")
try:
    logger.info(f">>>>>>>>>> Stage {STAGE_NAME} Started <<<<<<<<<<\n\n")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>> Stage {STAGE_NAME} Completed <<<<<<<<<<\n\n")

except Exception as e:
    raise CustomException(e,sys)


STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>>>>>> Stage {STAGE_NAME} Started <<<<<<<<<<\n\n")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>> Stage {STAGE_NAME} Completed <<<<<<<<<<\n\n")

except Exception as e:
    raise CustomException(e,sys)



STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>>>>>>> Stage {STAGE_NAME} Started <<<<<<<<<<\n\n")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>> Stage {STAGE_NAME} Completed <<<<<<<<<<\n\n")

except Exception as e:
    raise CustomException(e,sys)



STAGE_NAME = "Model Trainer Stage"
try:
    logger.info(f">>>>>>>>>> Stage {STAGE_NAME} Started <<<<<<<<<<\n\n")
    obj = ModelTrainerTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>> Stage {STAGE_NAME} Completed <<<<<<<<<<\n\n")

except Exception as e:
    raise CustomException(e,sys)




STAGE_NAME = "Model evaluation stage"
os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/Shivraj-Jadhav/Data_science_project_with_mlflow.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"]="Shivraj-Jadhav"
os.environ["MLFLOW_TRACKING_PASSWORD"]="your_password"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = ModelEvaluationTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise CustomException(e,sys)
