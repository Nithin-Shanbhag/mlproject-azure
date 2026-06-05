from setuptools import find_packages, setup
## find_packages = automatically find all the packages that are available in the ML application.
## In the folders which contain __init__.py file are considered as packages. 
## For example, src folder.
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:   ## read by default
        requirements=file_obj.readlines()
        
        ## removing the new line character from the requirements
        requirements=[req.replace("\n","") for req in requirements]
        
        ## remoing the -e . from the requirements
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements



## metadata of the project
setup(
    
    name='mlproject',
    version='0.0.1',
    author='Nithin Shanbhag',
    author_email='nnithinshanbhag@gmail.com',
    packages=find_packages(),
    ## install_requires=['pandas','numpy','seaborn']
    ## it is not feasible to write all the libraries in the install_requires.
    ## So we will create a requirements.txt file and write all the libraries in that file and 
    ## then we will read that file and pass the list of libraries to the install_requires.
    install_requires=get_requirements('requirements.txt')
    
)