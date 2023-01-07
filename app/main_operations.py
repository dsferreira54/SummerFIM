from app.scan import *
from app.checksum import *
from app.files_operations import *
from app.settings_yaml_vars import *
import os

class MainOperations:
    def init(pathToScan, filesListWithHashesTextFilePath):
        summerDataPath = str(SettingsYamlVars.filesListWithHashesTextFilePath)
        lastSlashOccurenceIndexInSummerDataPath = summerDataPath.rfind('/')
        summerDataPath = summerDataPath[:lastSlashOccurenceIndexInSummerDataPath]

        alreadyExists = os.path.exists(summerDataPath)

        if alreadyExists == False:
            os.makedirs(summerDataPath)

        filesList = Scan.path(pathToScan)
        filesListWithHashes = Checksum.sha2(filesList)
        FilesOperations.saveArrayInTextFile(filesListWithHashes, filesListWithHashesTextFilePath)

    def update(pathToScan, filesListWithHashesTextFilePath):
        currentFilesListWithoutHashes = Scan.path(pathToScan)
        oldFilesListWithHashes = Scan.textFile(filesListWithHashesTextFilePath)
        currentFilesListWithHashes = Checksum.sha2UpdateList(oldFilesListWithHashes, currentFilesListWithoutHashes)
        FilesOperations.backup(filesListWithHashesTextFilePath)
        FilesOperations.saveArrayInTextFile(currentFilesListWithHashes, filesListWithHashesTextFilePath)

    def help():
        print('help \t Display this help.')
        print('init \t First checksum of selected path in settings.yaml file.')
        print('update \t Update checksum of selected path in settings.yaml file.')
        print('exit \t Exit SummerFIM.')