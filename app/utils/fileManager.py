import yaml
import os
import glob

def loadDataFrom(filePathName):
        """
        filePathName: full path and name of the file to be loaded
        """
        with open(file=filePathName, mode='r', encoding='utf-8') as anyFile:
            print(f"Loading data from {filePathName}")
            fileData = yaml.safe_load(anyFile)
            print("Closing refered file")
            anyFile.close()
            return fileData


def updateFile(newData, filePathName):
    """
    newData: data structure to be loaded at filePathName
    filePathName: target file for data to be loaded
    """
    with open(file=filePathName, mode='w', encoding='utf-8') as anyFile:
        print(f"Dumping data into target file")
        yaml.dump(newData, anyFile)


def loadConfigFile():
    configFile = {}

    glob_path = os.environ['TRUE_PERF_APP_DIR']
    for config_file in glob.glob(os.path.join(glob_path, 'config.yaml')):
        with open(config_file, 'r') as f:
            configFile.update(yaml.safe_load(f))
    return configFile

configFile = loadConfigFile()
print(configFile['inputFilesPath'])