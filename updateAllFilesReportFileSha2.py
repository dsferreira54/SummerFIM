import os, fnmatch
import hashlib

# VARIABLES 
path = 'C:\\Users\David S. Ferreira\\Documents\\Teste'
path = 'F:\\'
allFilesReportFile = 'C:\\Users\\David S. Ferreira\\workdir\\VyramFIM\\allFilesReportFile.sha2'
allFilesReportFileOld = 'C:\\Users\\David S. Ferreira\\workdir\\VyramFIM\\allFilesReportFileOld.sha2'
allFilesArray = []
importedAllFilesArray = []
pattern = '*'
errorCounter = 0

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

# IMPORT OLD ALL FILES ARRAY FROM TXT
oldAllFilesReportFile_Object = open(allFilesReportFile, encoding="utf-8")
importedAllFilesArrayTemp = [x[:-1] for x in oldAllFilesReportFile_Object.readlines()]
importedAllFilesArray = [x[66:] for x in importedAllFilesArrayTemp]
oldAllFilesReportFile_Object.close()
importedAllFilesArray = sorted(importedAllFilesArray)

# CREATE ALL FILES ARRAY
for dName, sdName, fList in os.walk(path):
    for fileName in fList:
        if fnmatch.fnmatch(fileName, pattern):
            allFilesArray.append(os.path.join(dName, fileName))
allFilesArray = sorted(allFilesArray)

# COMPARING ARRAYS TO FIND OUT WHICH FILES WERE DELETED
deletionsArray = list(set(importedAllFilesArray) - set(allFilesArray))
deletionsArray = sorted(deletionsArray)


# COMPARING ARRAYS TO FIND OUT WHICH FILES WERE ADDED
additionsArray = list(set(allFilesArray) - set(importedAllFilesArray))

# REMOVING THE ITEMS PRESENT IN THE DELETIONARRAY IN THE importedALLFILESARRAY
temp = []
for element in importedAllFilesArrayTemp:
    if element[66:] not in deletionsArray:
        temp.append(element)
importedAllFilesArray = temp
temp = []
importedAllFilesArrayTemp = []

# CALCULATING HASH OF ADDITIONSARRAY
additionsArrayLenght = len(additionsArray)
currentIndexadditionsArray = 0
for i in additionsArray:
    currentIndexadditionsArray +=1
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
        temp.append(outputSha256 + ' *' + i)
        # print(BOLD + "[ " + OKGREEN + str(currentIndexadditionsArray) + '/' + str(additionsArrayLenght) + ENDC + " ] " + ENDC + outputSha256 + ' *' + i)
additionsArray = temp
temp = []

# JOINING importedALLFILESARRAY AND ADDITIONSARRAY
additionsArray = sorted(additionsArray, key=lambda x:x[66:])
importedAllFilesArray = importedAllFilesArray + additionsArray
importedAllFilesArray = sorted(importedAllFilesArray, key=lambda x:x[66:])

# WRITING IMPORTED ARRAY IN A TXT FILE
try:
    os.remove(allFilesReportFileOld)
except Exception:
    print(WARNING + '[WARNING] allFilesReportFileOld.sha2 does not exists.' + ENDC)
os.rename(allFilesReportFile, allFilesReportFileOld)
allFilesReportFile_Object = open(allFilesReportFile, 'a', encoding="utf-8")
for i in importedAllFilesArray:
    allFilesReportFile_Object.write(i + '\n')
allFilesReportFile_Object.close()

print("")
print("===================================== DEL ========================================")
print("")

deletionsArrayLenght = len(deletionsArray)
currentIndexDeletionsArray = 0
for i in deletionsArray:
    currentIndexDeletionsArray +=1
    print(BOLD + "[ " + OKGREEN + str(currentIndexDeletionsArray) + '/' + str(deletionsArrayLenght) + ENDC + " ] " + ENDC + i)

print("")
print("===================================== ADD ========================================")
print("")

additionsArrayLenght = len(additionsArray)
currentIndexAdditionsArray = 0
for i in additionsArray:
    currentIndexAdditionsArray +=1
    print(BOLD + "[ " + OKGREEN + str(currentIndexAdditionsArray) + '/' + str(additionsArrayLenght) + ENDC + " ] " + ENDC + i)
print("")