'''
## Short summary:
# dataclass decorator - use if only init functionality is needed 
 inside class
# @dataclasses we use when we need to store only variables , 
 it saves time & space as we no need to write constructor
# dataingestionconfig class - to define the train, test and 
 raw data path
# dataingestion class - 
# create instance var (ingestion_config) inside init for dataingestionconfig class
# Inside initiate_data_ingestion method
# read the data
# make dirs for whichever is present in the path in dataingestionconfig class
# dump the raw data in raw data path
# split the data into train and test
# dump the train and test data in respective paths
# return the train and test data path
'''




import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
## used to create class variables

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_trainer import ModelTrainer
from src.components.model_trainer import ModelTrainerConfig


@dataclass
## this will directly define class variables without using __init__ method
## if only init functionality is required, then we can use dataclass
class DataIngestionConfig:
    ## any input required for data ingestion can be added here as class variables
    train_data_path: str=os.path.join('artifacts','train.csv')
    ## save train data in above path
    test_data_path: str=os.path.join('artifacts','test.csv')
    raw_data_path: str=os.path.join('artifacts','data.csv')
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        ## inside ingestion_config var, we have sub var

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv('notebook/data/stud.csv')
            logging.info("Read the dataset as dataframe")
            
            ## make artifact directory if not exist
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            
            ## save the raw data in data.csv
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            
            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            
            logging.info("Ingestion of the data is completed")
            
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)
        



        
if __name__ == "__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()
    ## this is train and test data path
    
    data_transformation=DataTransformation()
    train_arr,test_arr=data_transformation.initiate_data_transformation(train_data, test_data)
    ## this is transformed train and test data
    
    model_trainer=ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_arr, test_arr))
    ## prints r2 score of the best model