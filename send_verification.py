# encoding: utf-8
from dotenv import dotenv_values
from Util.util import *
from Util.Constants import *
import logging
import sys
import os
from datetime import datetime

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,datefmt="%H:%M:%S")
now = datetime.now()

pathExcel = "fileInput/"
fileListExcel = os.listdir(pathExcel)

#Loading Environment Variables based on Domain
try:
    env = "."+sys.argv[1]
except IndexError:
    env = ""
config = {
    **dotenv_values(".env{}".format(env))
    }

def main():
    config["LOGFILE"] = "logs/" + now.strftime("%Y%m%d-%H%M%S.log")
    result = {item : [] for item in VALID_TABS}
    read_excel(config, pathExcel, fileListExcel, result)
    logging.info("Stats:")
    print(USER_TAB + ": " + str(len(result[USER_TAB])))
    logging.info("Sending Verification:")
    verificate_users(config, result[USER_TAB])

if __name__ == "__main__":
    main()