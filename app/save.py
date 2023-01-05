import os

# CUSTOM TEXT
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

class Save:
    def saveArrayInTextFile(array, textFilePath):
        alreadyExists = os.path.exists(textFilePath)
        if alreadyExists:
            print(FAIL + "[FAILED] Can't save, file already exists, please remove: " + textFilePath + ENDC)
        elif alreadyExists == False:
            textFileObject = open(textFilePath, 'a', encoding="utf-8")
            for i in array:
                textFileObject.write(i + '\n')
            textFileObject.close()
        else:
            print("File already exists.")