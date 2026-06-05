'''
For example lets take try-except dlock, where in try I get div bby zero error
except block catches it and passes that exception as e
CustomException class will be invoked and I will pass e and sys, sys - to extract file number and line number of the error.
Inside CustomException class, under init method, e and sys will be passed and e will be passes to parent class
Exception and sys will be passed to error_message_details function, which will extract file name and line number of the error and return the error message we want.
When we print the object of CustomException class, it will return the error message.
'''

import sys
## sys - used to manipulate python runtime environment.
## Testing using logger module
from src.logger import logging



##  error=custom error message, error details = extracted from sys module
def error_message_details(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    ## info like file no. and line no. of the error occured.
    
    ## file in which error occurred
    file_name = exc_tb.tb_frame.f_code.co_filename
    ## line in which error occurred
    line_number = exc_tb.tb_lineno
    
    error_message = f"Error occurred in python script: [{file_name}] at line number: [{line_number}] error message: [{str(error)}]"
    
    return error_message


## defining custom exception class
class CustomException(Exception):
    ## will be passing on error message as parameter to custom exception object.
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        ## error message passed will be provided to error_message_details function
        ## and returns the error message we want.
        self.error_message = error_message_details(error_message, error_detail)
        
    ## when we print the object of this class, it will return the error message.
    def __str__(self):
        return self.error_message
    
    
    
'''
## Testing
if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by zero error occurred")
        raise CustomException(e, sys)
'''