from app.main_operations import *
from app.settings_yaml_vars import *

while True:
    # OPERATION CHOICE
    choiceOfOperation = input('summer> ')

    # OPERATION EXECUTION
    if choiceOfOperation=="help":
        MainOperations.help()
    elif choiceOfOperation=="init":
        MainOperations.init(SettingsYamlVars.pathToScan, SettingsYamlVars.filesListWithHashesTextFilePath)
    elif choiceOfOperation=="update":
        MainOperations.update(SettingsYamlVars.pathToScan, SettingsYamlVars.filesListWithHashesTextFilePath)
    elif choiceOfOperation=="exit":
        print('Bye bye!')
        break
    elif choiceOfOperation=="":
        pass
    else:
        print("Unknown option, type help to show all avaible commands.")