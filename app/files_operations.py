import os

# CUSTOM TEXT
INFO = '[ \033[94mINFO\033[0m ]'
ERROR = '[ \033[91mERROR\033[0m ]'
WARNING = '[ \033[93mWARNING\033[0m ]'

class FilesOperations:
    def saveArrayInTextFile(array, textFilePath):
        alreadyExists = os.path.exists(textFilePath)
        if alreadyExists:
            print(WARNING + " Can't save, file already exists.")
            while True:
                CHOICE = input("Do you want to replace " + textFilePath + "? ")
                if CHOICE == "yes":
                    print(INFO + " Replacing file...")
                    os.remove(textFilePath)
                    alreadyExists = False
                    break
                elif CHOICE == "no":
                    print(INFO + " Canceling operation...")
                    break
                else:
                    print(WARNING + " Unknown option, only yes or no.")
        if alreadyExists == False:
            textFileObject = open(textFilePath, 'a', encoding="utf-8")
            for i in array:
                textFileObject.write(i + '\n')
            textFileObject.close()

    def backup(fileToBackupPath):
        fileToBackupPath_str = str(fileToBackupPath)
        index = fileToBackupPath_str.rfind(".")
        backupFilePath = fileToBackupPath_str[:index] + "_old" + fileToBackupPath_str[index:]
        os.rename(fileToBackupPath, backupFilePath)