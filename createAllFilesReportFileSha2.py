import os, fnmatch
import hashlib

# VARIABLES 
path = 'C:\\Users\David S. Ferreira\\Documents\\Teste'
# path = 'F:\\'
allFilesReportFile = 'C:\\Users\\David S. Ferreira\\workdir\\VyramFIM\\allFilesReportFile.sha2'
pattern = '*'
allFilesArray = []
errorCounter = 0
currentIndexAllFilesArray = 0

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

# CREATE ALL FILES ARRAY
for dName, sdName, fList in os.walk(path):
    for fileName in fList:
        if fnmatch.fnmatch(fileName, pattern):
            allFilesArray.append(os.path.join(dName, fileName))
allFilesArray = sorted(allFilesArray)
allFilesArrayLenght = len(allFilesArray)

# WRITING ALL FILES ARRAY IN A TXT FILE CALLED ALL FILES REPORT FILE (AFRF)
allFilesReportFile_Object = open(allFilesReportFile, 'a', encoding="utf-8")
for i in allFilesArray:
    currentIndexAllFilesArray +=1
    sha256_hash = hashlib.sha256()
    try:
        with open(i,"rb") as f:
            for byte_block in iter(lambda: f.read(4096),b""):
                sha256_hash.update(byte_block)
            outputSha256 = sha256_hash.hexdigest()
            permissionErrorException = False
    except PermissionError:
        print(FAIL + '[ERROR] Checksum permission error on file: ' + i + '' + ENDC)
        errorCounter +=1
        permissionErrorException = True
    if permissionErrorException == False:
        allFilesReportFile_Object.write(outputSha256 + ' *' + i + '\n')
        print(BOLD + "[ " + OKGREEN + str(currentIndexAllFilesArray) + '/' + str(allFilesArrayLenght) + ENDC + " ] " + ENDC + outputSha256 + ' *' + i)
allFilesReportFile_Object.close()

# SHOWING OPERATION RESULTS
print('')
print("A operação terminou com " + str(errorCounter) + " erros.")