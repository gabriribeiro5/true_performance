# Dealing with ImportError: attempted relative import with no known parent package
import sys
sys.path.append('.')

# logging setup
from app.utils import fileManager
import os
import logging

def enableLog():
    fileName = fileManager.loadConfigFile()
    logFilePathAndName = os.path.join(os.environ['TRUE_PERF_LOG_DIR'], fileName['logFile'])

    logging.basicConfig(filename=logFilePathAndName, level=logging.DEBUG)
    # logging.FileHandler(filename=logFilePathAndName)
