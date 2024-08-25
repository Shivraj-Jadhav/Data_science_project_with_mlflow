# Data_science_project_with_mlflow
1. Data Ingestion:

Downloads a file from a specified URL and saves it locally.</br>
Checks if the file already exists and avoids redundant downloads.</br>
Extracts the data from a zip file if applicable.</br>
2. Data Validation:

Reads the downloaded CSV file.</br>
Checks for missing values and reports the status.</br>
Validates if all columns present in the data match the expected schema.</br>
3. Data Transformation:

Splits the data into training and testing sets using train_test_split from scikit-learn.</br>
Saves the resulting train and test datasets as separate CSV files.</br>
4. Model Trainer:

Defines a configuration class to hold model training parameters.</br>
Reads configurations from YAML files and sets hyper-parameters.</br>
Performs a grid search to identify the best hyper-parameters for the ElasticNet model.</br>
Trains the ElasticNet model on the training data with the chosen hyper-parameters.</br>
Saves the trained model using joblib.</br>
5. Model Evaluation:

Defines a configuration class for model evaluation parameters.</br>
Reads configurations from YAML files and sets evaluation parameters.</br>
Loads the trained model and test data.</br>
Evaluates the model's performance using metrics like RMSE, MAE, and R2.</br>
Logs model parameters, metrics, and evaluation scores to MLflow for tracking.</br>
Overall, the code demonstrates a well-organized and modular approach to building an ML pipeline. Here are some additional points to consider:

Error Handling: While there's basic exception handling using CustomException, consider adding more specific exceptions for different scenarios.</br>
Logging: The code uses basic info logging, you might want to explore more comprehensive logging libraries for detailed tracking.</br>
Configuration Management: Consider using environment variables or a dedicated configuration management tool for more flexible configuration management.</br>
Testing: Implementing unit tests for individual components would ensure code robustness.</br>


## Workflow

1. Setup 
2. config.yaml
3. schema.yaml
4. params.yaml
5. Entity
6. Configuration manager in src config
7. Components
8. Pipeline
9. main.py
10. app.py



# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/Shivraj-Jadhav/Data_science_project_with_mlflow
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mlproj python=3.8 -y
```

```bash
conda activate mlproj
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)


MLFLOW_TRACKING_URI=https://dagshub.com/Shivraj-Jadhav/Data_science_project_with_mlflow.mlflow

![2](https://github.com/user-attachments/assets/496ae69a-1efe-42dc-b587-da7016abad1a)

![1](https://github.com/user-attachments/assets/21d0bd17-1af2-4659-ade3-90f499de3f16)

![3](https://github.com/user-attachments/assets/71c465c7-6a31-4ada-88f6-bac118f58932)

![image](https://github.com/user-attachments/assets/08393099-59b3-46ec-9023-80d8d6aa8269)

![image](https://github.com/user-attachments/assets/11f882a8-ab90-4a5d-a6e0-7d2af63725c2)


# Deployment using Render.com

![image](https://github.com/user-attachments/assets/069b215c-a58a-4f38-9d98-965531fda60b)

![image](https://github.com/user-attachments/assets/7ec122a4-d7c6-46c9-a168-9f14101044cb)

![image](https://github.com/user-attachments/assets/997da9ee-457c-4fc3-a403-828e8f05c7a2)

![image](https://github.com/user-attachments/assets/cea9a438-2b38-4523-840a-d004c3a22bec)

![image](https://github.com/user-attachments/assets/153bc29d-9cd5-4681-9348-71166978044e)




