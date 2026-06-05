'''
define log filename, define log file path, create log directory if not exists, configure logging settings
'''

import logging
import os
from datetime import datetime

## log file naming convention
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
## path of log file to be stored
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
## making directory if not exists, append files in it if exists
os.makedirs(logs_path, exist_ok=True)

## path of the file in which log will be stored
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    # where to store logging info
    filename=LOG_FILE_PATH,
    # format of logging info
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    # use info level logging, it will log all the info, warning and error messages.
    # use logging.info() and write any print msg it will log it
    level=logging.INFO
)
## whenever we want to log something, we can use logging.info().

'''
## Testing this logger
if __name__=="__main__":
    logging.info("Logging has started")
'''

    