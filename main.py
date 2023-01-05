from app.scan import *
from app.check import *
from app.save import *

# IMPORTING SETTINGS YAML IN A ARRAY
settingsYamlArray = ScanSettingsYaml.scan()

# [VAR DECLARATION] IMPORTING KEY VALUES FROM settingsYamlArray
pathToScan = settingsYamlArray['pathToScan']
filesListWithHashTextFilePath = settingsYamlArray['filesListWithHashTextFilePath']
filesListWithHashTextFilePathBackup = settingsYamlArray['filesListWithHashTextFilePathBackup']

# [VAR DECLARATION] OTHER VARS
choiceOfOperation = input('What do you me want to do: ') # CAN BE: "setup," "init", "update", "check", "delete"

# SCANING pathToScan AND CREATING A LIST OF A ALL FILES IN THE PATH
filesList = ScanPath.scan(pathToScan)

# OPERATION CHOICE
if choiceOfOperation=="init":
    print("let's init!")
    print("")
    filesListWithHash = Checksum.sha2(filesList)
    Save.saveArrayInTextFile(filesListWithHash, filesListWithHashTextFilePath)

# elif choiceOfOperation=="update": # TO DO
#     print("let's update!")
#     print("")
#     importedFilesListWithHash = ScanHashFile.importFileDataInArray(filesListWithHashTextFilePath)

# elif choiceOfOperation=="check": # TO DO
#     print("let's check!")
#     print("")
#     Integrity.check(filesList, filesListWithHashTextFilePath)
    
else:
    print("Error")
