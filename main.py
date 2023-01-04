from app.scan import *

# IMPORTING YAML KEY VALUES AS VARIABLES
yamlArray = ScanYaml.scan()

pathToScan = yamlArray['pathToScan']
hashFile = yamlArray['hashFile']


# TESTING ScanPath.scan
print(ScanPath.scan(pathToScan))