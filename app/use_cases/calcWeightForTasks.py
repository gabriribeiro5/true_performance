'''
Use variables from data.input.setbacks.yaml to calc
    additionalWeight=(subweight1 + subweight2 + subweight3)/subtasksCount

Apply additionalWeight to data.output.commonTasks.yaml
'''

from utils import fileManager

import yaml

#Set external variables
inputFilesPath = r'/home/kraken/codes/true_performance/app/data/input/' # r'path' turns path-like object into raw string
outputFilesPath = r'/home/kraken/codes/true_performance/app/data/output/'
configFilesPath  = r'/home/kraken/codes/true_performance/app/configfiles/'
setbacksFile = 'setbacks.yaml'
commonTasksFile = 'commonTasks.yaml'
configFileName = 'conf.yaml'

class weight_tasks_class(object, taskCategory, taskName, srcFilePathName, targetFilePathName):
    """taskCategory:
        taskName:
        srcFilePathName:
        targetFilePathName:
    """

    def __init__(self, arg, taskType):
        super(weight_tasks_class, self).__init__()
        self.arg = arg
        self.taskType = taskType
        self.srcFilePathName = srcFilePathName
        self.targetFilePathName = targetFilePathName
        self.setbacksPathName = f'{inputFilesPath}{setbacksFile}' # f'{var1}{var2}' allows concatenating variables into str mode
        self.commonTasksPathName = f'{outputFilesPath}{commonTasksFile}'
        self.configFilePathName = f'{configFilesPath}{configFileName}'
        print("Looking for setbacks at: "+self.setbacksPathName)

    print(f"Opening source file")
    setbacksData = fileManager.loadDataFrom(srcFilePathName)

    print(f"Opening target file")
    tasksData = fileManager.loadDataFrom(targetFilePathName)

    def addUpWeight(setbacksData, tasksData):
        """
        filePathName: full path and name of the file to be loaded

        """
        print(f"Adding setbacks weight to commonTasksFile")
        for stbk in setbacksData:
            if taskName in stbk['RELATED_TASK_CATEGORY']:
                for subtask in stbk['RELATED_SUBTASKS']:
                    tasksData[{taskCategory}][{taskName}][WEIGHT] += stbk['WEIGHT']

    print("-----------------------------------------------------------------")

    updateFile(tasksData, targetFilePathName)
    loadDataFrom()

    print("==================================================================")


# performanceRate = resultingWeight * stbk['RECURRENCY']
