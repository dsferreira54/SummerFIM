import os, fnmatch
import yaml

class Scan:
    def yaml(yamlFilepath):
        with open(yamlFilepath) as yamlFile: 
            yamlArray = yaml.safe_load(yamlFile)

        return yamlArray

    def path(pathToScan):
        path = str(pathToScan)
        pattern = '*'
        filesListArray = []

        for dName, sdName, fList in os.walk(path):
            for fileName in fList:
                if fnmatch.fnmatch(fileName, pattern):
                    filesListArray.append(os.path.join(dName, fileName))
        filesListArray = sorted(filesListArray)

        return filesListArray

    def textFile(path):
        textFileObject = open(path, encoding="utf-8")
        textFileArray = [i[:-1] for i in textFileObject.readlines()]

        textFileObject.close()

        textFileArray = sorted(textFileArray)

        return textFileArray