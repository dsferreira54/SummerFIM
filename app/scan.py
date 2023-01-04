import os, fnmatch
import yaml

class ScanPath:
    def scan(pathToScan):
        path = str(pathToScan)
        pattern = '*'
        allFilesArray = []

        for dName, sdName, fList in os.walk(path):
            for fileName in fList:
                if fnmatch.fnmatch(fileName, pattern):
                    allFilesArray.append(os.path.join(dName, fileName))
        allFilesArray = sorted(allFilesArray)
        allFilesArrayLenght = len(allFilesArray)

        return allFilesArray, allFilesArrayLenght

class ScanYaml:
    def scan():
        yamlFilepath = r"app/settings/settings.yaml"

        with open(yamlFilepath) as yamlFile: 
            yamlArray = yaml.safe_load(yamlFile)

            return yamlArray