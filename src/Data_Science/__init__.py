import os
import logging
import sys


logging_start="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir="logs"
log_filepath=os.path.join(log_dir,"logging.log")
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_start,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)
logger=logging.getLogger("datasciencelogger")
