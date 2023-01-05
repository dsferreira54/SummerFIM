import os, fnmatch
import yaml

class ScanSettingsYaml:
    def scan():
        yamlFilepath = r"app/settings/settings.yaml"

        with open(yamlFilepath) as yamlFile: 
            yamlArray = yaml.safe_load(yamlFile)

            return yamlArray

class ScanPath:
    def scan(pathToScan):
        path = str(pathToScan)
        pattern = '*'
        filesListArray = []

        for dName, sdName, fList in os.walk(path):
            for fileName in fList:
                if fnmatch.fnmatch(fileName, pattern):
                    filesListArray.append(os.path.join(dName, fileName))
        filesListArray = sorted(filesListArray)

        return filesListArray

class ScanHashFile:
    def importFileDataInArray():
        return #importHashFile #todo