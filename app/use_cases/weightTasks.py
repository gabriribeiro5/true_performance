'''apply weight to micro-tasks and gennerate a performance rate

CODE SOURCE:
    - How to update yaml file [https://stackoverflow.com/questions/68617796/how-to-update-the-values-of-yaml-file-using-python-code]

'''

import yaml

#Set external variables
inputFilesPath = r'/home/kraken/codes/true_performance/app/data/input/' # r'path' turns path-like object into raw string
outputFilesPath = r'/home/kraken/codes/true_performance/app/data/output/'
configFilesPath  = r'/home/kraken/codes/true_performance/app/configfiles/'
setbacksFile = 'setbacks.yaml'
commonTasksFile = 'commonTasks.yaml'
configFileName = 'conf.yaml'

#Set module variables
setbacksPathName = f'{inputFilesPath}{setbacksFile}' # f'{var1}{var2}' allows concatenating variables into str mode
commonTasksPathName = f'{outputFilesPath}{commonTasksFile}'
configFilePathName = f'{configFilesPath}{configFileName}'
print("Looking for setbacks at: "+setbacksPathName)

def loadDataFrom(filePathName):
    with open(file=filePathName, mode='r', encoding='utf-8') as anyFile:
        print(f"Loading data from {filePathName}")
        fileData = yaml.safe_load(anyFile)
        print("Closing refered file")
        anyFile.close()
        return fileData

def updateFile(newData, filePathName):
    with open(file=filePathName, mode='w', encoding='utf-8') as anyFile:
        print(f"Dumping data into target file")
        yaml.dump(newData, anyFile)

def weightTransactions(srcFilePathName, targetFilePathName):
    'distributes wheight to each transaction in data.output.commonTasks acording to data.input.setbacks'
    print("")
    print("================ Applying wheight to commonTasks ================")
    print("")

    print(f"Opening source file")
    setbacksData = loadDataFrom(srcFilePathName)
    print(f">> first setback is: {setbacksData['STBK1']['DESCRIPTION']}")

    print("-----------------------------------------------------------------")

    print(f"Opening target file")
    tasksData = loadDataFrom(targetFilePathName)
    print(f">> first task is: {tasksData['INTERNATIONAL']}")

    print("-----------------------------------------------------------------")

    updateFile(tasksData, targetFilePathName)

    print("==================================================================")


weightTransactions(setbacksPathName, commonTasksPathName)

def calcPerf():
    pass
