'''apply weight to micro-tasks and gennerate a performance rate

CODE SOURCE:
    ruamel.yaml:
    - How to update yaml file [https://stackoverflow.com/questions/28557626/how-to-update-yaml-file-using-python]
    - 
'''

# import os
# import sys
# from typing import Counter
from collections import Counter
import yaml
# import ruamel.yaml

# file_name = 'input.yaml'
# config, ind, bsi = ruamel.yaml.util.load_yaml_guess_indent(open(file_name))

# instances = config['instances']
# instances[0]['host'] = '1.2.3.4'
# instances[0]['username'] = 'Username'
# instances[0]['password'] = 'Password'

# with open('output.yaml', 'w') as fp:
#     yaml.dump(config, fp)


configfilesPath = 'c://Users/User/weighted_services//'
setbacksFile = 'setbacks.yaml'
commonTasksFile = 'commonTasks.yaml'
setbacksPathName = f'{configfilesPath}{setbacksFile}'
commonTasksPathName = f'{configfilesPath}{commonTasksFile}'
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
        print("Closing source file")
        stbkFile.close()

        for stbk, sValue in setbacks.items():
            print("")
            weight = sValue['WEIGHT']
            RELATED_TRANSACTION_CATEGORY = sValue['RELATED_TRANSACTION_CATEGORY']
            RELATED_SUBTASKS = sValue['RELATED_SUBTASKS']
            print(f"Opening target file")

            with open(file=targetFilePathName, mode='r', encoding='utf-8') as tasksFile:
                print(f"Loading target file to memory")
                tasks = yaml.safe_load(tasksFile)
                print(tasks)
                print("Closing target file")
                tasksFile.close()
                for task, tValue in setbacks.items():
                    print("")
            print("=====================================================================================================")
            

weightTransactions(setbacksPathName, commonTasksPathName)

def calcPerf():
    pass