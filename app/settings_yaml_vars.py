from app.scan import *

class SettingsYamlVars:
    settingsYamlArray = Scan.yaml('app/settings/settings.yaml')

    pathToScan = settingsYamlArray['pathToScan']
    filesListWithHashesTextFilePath = settingsYamlArray['filesListWithHashesTextFilePath']