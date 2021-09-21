'''apply weight to micro-tasks and gennerate a performance rate

CODE SOURCE:
    ruamel.yaml:
    - How to update yaml file [https://stackoverflow.com/questions/28557626/how-to-update-yaml-file-using-python]
    - 
'''

# import os
# import sys
# from typing import Counter
# from collections import Counter
import yaml
# import ruamel_yaml

# file_name = 'input.yaml'
# config, ind, bsi = ruamel_yaml.util.load_yaml_guess_indent(open(file_name))

# instances = config['instances']
# # instances[0]['host'] = '1.2.3.4'
# # instances[0]['username'] = 'Username'
# # instances[0]['password'] = 'Password'

# with open('output.yaml', 'w') as fp:
#     yaml.dump(config, fp)

#Set external variables
inputFilesPath = r'c:/Users/User/true_performance/app/data/input/' # r'path' turns path-like object into raw string
outputFilesPath = r'c:/Users/User/true_performance/app/data/output/'
configFilesPath  = r'c:/Users/User/true_performance/app/configfiles/'
setbacksFile = 'setbacks.yaml'
commonTasksFile = 'commonTasks.yaml'
configFileName = 'conf.yaml'

#Set module variables
setbacksPathName = f'{inputFilesPath}{setbacksFile}' # f'{var1}{var2}' allows concatenating variables into str mode
commonTasksPathName = f'{outputFilesPath}{commonTasksFile}'
configFilePathName = f'{configFilesPath}{configFileName}'
print("Looking for setbacks at: "+setbacksPathName)


def weightTransactions(srcFilePathName, targetFilePathName):
    'distributes wheight to each transaction in configfiles.commonTasks acording to configfiles.setbacks'
    print("")
    print("================ Applying wheight to commonTasks ================")
    print("")
    print(f"Opening source file")
    with open(file=srcFilePathName, mode='r', encoding='utf-8') as stbkFile:
        print(f"Loading source file data to memory")
        setbacks = yaml.safe_load(stbkFile)
        print(f">> first setback is: {setbacks['STBK1']['DESCRIPTION']}")
        print("Closing source file")
        stbkFile.close()

    print("-----------------------------------------------------------------")

    with open(file=targetFilePathName, mode='r', encoding='utf-8') as tasksFile:
        print(f"Loading target file to memory")
        tasksData = yaml.safe_load(tasksFile)
        print("Closing target file")
        tasksFile.close()

    print("-----------------------------------------------------------------")

    with open(file=targetFilePathName, mode='w', encoding='utf-8') as tasksFile:
        print(f"Dumping data into target file")
        yaml.dump(tasksData, tasksFile)

    print("==================================================================")
            

weightTransactions(setbacksPathName, commonTasksPathName)

def calcPerf():
    pass