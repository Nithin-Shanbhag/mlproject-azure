'''
import necessary libraries
create a flask object
create a route for home page that renders the index.html page
create a folder named templates in working directory
    and create a file named index.html in templates folder, 
    with some html code in it
create a route for predictdata that accepts both GET and POST request
    if request method is GET then render the home.html page
    else if request method is POST then do the following:
        Create an object of CustomData class and 
        pass the extracted data to it to get the data in dataframe format
        (check out predict pipeline.py file for CustomData class)
        Create an object of PredictPipeline class and 
        call the predict function of it to get the predicted value
        (check out predict pipeline.py file for PredictPipeline class)
        render the home.html page with the predicted value
'''

from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)

app = application

## route for home page

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET','POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')  ## contains the form to take input data from user
    else:
        ## before proceeding further, check out the prediction pipeline code
        data = CustomData(
            gender=request.form['gender'],
            race_ethnicity=request.form['race_ethnicity'],
            parental_level_of_education=request.form['parental_level_of_education'],
            lunch=request.form['lunch'],
            test_preparation_course=request.form['test_preparation_course'],
            reading_score=int(request.form['reading_score']),
            writing_score=int(request.form['writing_score'])
        )       ## Fetch data from form and pass it to CustomData class
        
        pred_df = data.get_data_as_dataframe()
        ## convert the data into dataframe
        
        predict_pipeline = PredictPipeline()
        ## create a predict pipeline object
        
        results = predict_pipeline.predict(pred_df)
        ## call the predict function of predict pipeline to get the predicted value
        
        return render_template('home.html', results=results[0])
        ## render the home.html page with the predicted value


if __name__=="__main__":
    app.run(host="0.0.0.0")
    ## type 127.0.0.1:5000/ in browser to see homepage
    ## type 127.0.0.1:5000/predictdata in browser to see the prediction page
    ## debug = true should be removed in production environment, it is only for development purpose