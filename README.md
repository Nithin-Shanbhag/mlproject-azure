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

Deployment in AWS Elastic Beanstock:
Configurations to be done:
- Create .ebextensions folder in working directory
- Insdie the folder, create python.config file - used to tell elastic beanstock instance that what is the entry point of the application
- In python.config, define container as python and WSGIPath (Flask app entry point) as application:application (1st one indicates the Flask app file name, 2nd one indicates the Flask object name in the file)
- Ensure to remove debug=true in application.py

- push the config to github repo

- Login to AWS management condole, search elastic beanstalk, hover the mouse over it and click on application, got to elastic beanstalk, here you will observe Create application button.

- Theory on deployment:
AWS Elastic beanstalk is a server/cloud environment of linux instance where I can create an evironment or deploy a code. My code resides in git hub repo and the configuration required by beanstalk is in python.config . To deploy code and any changes done to it from github to cloud, we use code pipeline. Whenever any changes to code is done, it is automatically deployed on click of a button - Do you want to deploy this code. This pipeline is called continuous delivery pipeline. 
So step 1 is to create elastic beanstalk instance and also creating an environment. step 2 is to integrate codepipeline with github repo and do continuous deploymwent into elastic beanstalk.

- (Continuation) Click on create application, application name: studentperformance, platform: python, application code: sample application - create application (takes some time to create application)

Now lets create code pipeline and integrate it with our github repo:
- AWS management console, search: codepipeline (release software for continuous delivery), click on it.
- Create pipeline
- category: build custom pipeline, next
- pipeline name: studentperformance, next
- source provider: Github via Github app, click connect to github, connect name: studentperformance, connect, repo name: Nithin-Shanbhag/mlproject, branch: main, next
- skip build stage
- skip test stage
- deploy provider: AWS Elastic Beanstalk, app name: studentperformance, env name: Studentperformance-env, next
- click on create pipeline only after the environment is set

Challenge: Here I encountered deployment error, because while installing dependencies, xgboost package in requirements.txt was installing a huge file: nvidia_nccl_cu12-2.30.4-py3-none-manylinux_2_18_x86_64.whl (300.2 MB)
Hence I removed xgboost from the requirements.txt file.

- click on aws elastic beanstalk link after successful deployment
- click on the url, observe our web application

web application homepage url: http://studentperformance1-env.eba-qrpw5nfp.ap-southeast-2.elasticbeanstalk.com/
web application homepage url: http://studentperformance1-env.eba-qrpw5nfp.ap-southeast-2.elasticbeanstalk.com/predictdata

