'''
The web application will be extracting the input data from the form
and passing on to the Custom data class which will convert form data into dataframe
This Dataframe is passed to predict pipeline which will do the following:
load the preprocessor object and the model object
transform the input data using preprocessor object
predict the target variable using model object and 
return the predicted value to the web application
'''

import sys
import os
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    ## This function will load the preprocessor and model objects and
    ## transform the input data and predict the target variable
    ## and return the predicted value to the web application
    def __init__(self):
        pass
    
    def predict(self, features):
        try:
            preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')
            model_path = os.path.join('artifacts', 'model.pkl')
            preprocessor = load_object(preprocessor_path)
            model = load_object(model_path)
            data_scaled = preprocessor.transform(features)
            pred = model.predict(data_scaled)
            
            return pred
        
        except Exception as e:
            raise CustomException(e, sys)
        
class CustomData:           
    def __init__(self,
                 gender: str,
                 race_ethnicity: str,
                 parental_level_of_education: str,
                 lunch: str,
                 test_preparation_course: str,
                 reading_score: int,
                 writing_score: int):
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    def get_data_as_dataframe(self):
        ## This function will convert the data into dataframe
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score]
            }
            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e, sys)