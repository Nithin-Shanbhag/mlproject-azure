'''
import libraries as and when required
In save object function, we are saving the object passed into the file_path passed
    extract the directories from file_path and make dirs if not exists
    open the file_path in write mode and dump the object in file using dill
In evaluate_models function, we are training, predicting and evaluating the model with hyperparameter tuning using GridSearchCV
    and returning the report containing test model score for each model.
'''

import os
import sys

import numpy as np
import pandas as pd
from sklearn.model_selection import GridSearchCV

import dill
from sklearn.metrics import r2_score
from src.exception import CustomException

## saving the object in the given path (pickle file)
def save_object(file_path, obj):
    try:
        ## dirname will consider path except filename
        ## and makedirs will create the directory if not exist
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
    
## train the model, predict and evaluate it with hyperparameter tuning using GridSearchCV
def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    try:
        report = {}
        for i in range(len(models)):
            model = list(models.values())[i]
            para = param[list(models.keys())[i]]
            
            gs = GridSearchCV(model, para, cv=3)
            gs.fit(X_train, y_train)
            
            model.set_params(**gs.best_params_)
            
            model.fit(X_train, y_train)
            
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)
            
            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)
    
## loading the object from the given path (pickle file)
def load_object(file_path):
    try:
        with open(file_path, 'rb') as file_obj:
            return dill.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)