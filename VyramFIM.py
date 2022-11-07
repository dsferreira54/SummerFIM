import os, fnmatch
import hashlib

# VARIABLES 
path = 'F:\Documentos\Virtual Machines'
# path = 'F:\\'
allFilesReportFile = 'C:\\Users\\David S. Ferreira\\workdir\\VyramFIM\\allFilesReportFile.sha2'
pattern = '*'
allFilesArray = []

# CREATE ALL FILES ARRAY
for dName, sdName, fList in os.walk(path):
    for fileName in fList:
        if fnmatch.fnmatch(fileName, pattern):
            allFilesArray.append(os.path.join(dName, fileName))
allFilesArray = sorted(allFilesArray)

# WRITING ALL FILES ARRAY IN A TXT FILE CALLED ALL FILES REPORT FILE (AFRF)
allFilesReportFile_Object = open(allFilesReportFile, 'a', encoding="utf-8")
for i in allFilesArray:
    sha256_hash = hashlib.sha256()
    with open(i,"rb") as f:
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
        outputSha256 = sha256_hash.hexdigest()
    allFilesReportFile_Object.write(outputSha256 + ' *' + i + '\n')
    print(outputSha256 + ' *' + i)
allFilesReportFile_Object.close()
