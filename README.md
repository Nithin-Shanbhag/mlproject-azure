# Student performance prediction project

## Goal: Estimate how student's performance (test scores) is affected by other variables such as Gender, Ethnicity, Parental level of education, Lunch and Test preparation course.

## Software and tool requirement
1. [Github Account](https://github.com)
2. [Heroku Account](https://heroku.com)
3. [VS Code IDE](https://code.visualstudio.com/)
4. [GitCLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)

### Step 1:

Create a new environment for the project

```
conda create -p venv python==3.14 -y
```
Activate it

```
conda activate venv/
```

### Step 2:

Create a [requirements.txt](requirements.txt) file which contains all libraries that needs to be installed.

### Step 3:

- Create a [setup.py](setup.py) file which will be responsible for creating ML application as a package.
- Also create a [src](src) folder with '__init__.py' file in it.

- Now run the command:
```
pip install -r requirements.txt
```

### Step 4:

- Create a folder inside src called [components](src/components) and create a '__init__.py' file inside it because components can be created as a package.
- Components folder will hold all the modules that are going to be created.
1. [data_ingestion.py](src/components/data_ingestion.py) - collecting the data
2. [data_transformation.py](src/components/data_transformation.py) - feature engineering
3. [model_trainer.py](src/components/model_trainer.py) - training the model

### Step 5:

- Create [logger.py](src/logger.py) for logging purposes.
- Create [exception.py](src/exception.py) for exception handling purposes.
- Create [utils.py](src/utils.py) for functionalities used in a common way.

### Step 6:

Notebook folder contains dataset and jupyter notebooks containing EDA and model training code.
[dataset](notebook/data/stud.csv)
[EDA](<notebook/1 . EDA STUDENT PERFORMANCE .ipynb>)
[Model training](<notebook/2. MODEL TRAINING.ipynb>)

### Step 7:

Write code in [data_ingestion.py](src/components/data_ingestion.py), [data_transformation.py](src/components/data_transformation.py) and [model_trainer.py](src/components/model_trainer.py)
Detailed explanation provided in these files.

### Step 8:

Now I have pickle files for preprocessor and model, lets predict on new data:
- Create the predict_pipeline.py file - contains function to transform the input data to dataframe and return dataframe (CustomData) & a function to load the pickle files, perform transformation on feature data and return prediction (PredictPipeline).
- Create load_object function in utils.py file - to load the pickle file from the file path passed to it.
- Create a flask web application - Create a homepage and /predictdata page. The latter contains a page which displays form for user input and upon submit, it will display predicted output.

### Step 9:

- Login to MS Azure account
- Create a reaource
- Web app, Create
- subscription: (default value), resource group: testgroupregression, name: studentperformanceprediction, publish: code, runtime stack: python 3.14, OS: Linux, region: south india, click on next till deployment tab
- continuous deployment: enable, github account: authorize, select organization, repository and branch from drop down, click on review+create
- review it and click on create
Challenge: initially received error - insufficient VMs for deployment. resolution: changes region from canada (default) to south india.
- After build and deploy is complete, search for your web app and click on the domain link.
Observe your app running.
Observe in your github repository .yml file is created and under actions tab, see build and deploy.