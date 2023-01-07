import hashlib

# CUSTOM TEXT
INFO = '[ \033[94mINFO\033[0m ]'
ERROR = '[ \033[91mERROR\033[0m ]'
WARNING = '[ \033[93mWARNING\033[0m ]'
OKGREEN = '\033[92m'
OKYELLOW = '\033[93m'
BOLD = '\033[1m'
ENDC = '\033[0m'

class Checksum:
    def sha2(filesList):
        temp = []
        filesListLenght = len(filesList)
        currentIndexfilesList = 0
        for i in filesList:
            currentIndexfilesList +=1
            sha256_hash = hashlib.sha256()
            try:
                with open(i,"rb") as f:
                    for byte_block in iter(lambda: f.read(4096),b""):
                        sha256_hash.update(byte_block)
                    outputSha256 = sha256_hash.hexdigest()
                    permissionErrorException = False
            except PermissionError:
                print(ERROR + ' Checksum permission error on file: ' + i)
                errorCounter +=1
                permissionErrorException = True
            if permissionErrorException == False:
                temp.append(outputSha256 + ' *' + i)
                print(BOLD + "[ " + OKGREEN + str(currentIndexfilesList) + '/' + str(filesListLenght) + ENDC + " ] " + ENDC + outputSha256 + ' *' + i)
        filesList = temp
        temp = []

        return filesList

    def sha2UpdateList(oldFilesListWithHashes, newFilesListWithoutHashes):
        
        oldFilesListWithoutHashes = [i[66:] for i in oldFilesListWithHashes]

        # COMPARING ARRAYS oldFilesListWithoutHashes AND newFilesListWithoutHashes TO FIND OUT WHICH FILES WERE DELETED
        filesDeletionsArray = list(set(oldFilesListWithoutHashes) - set(newFilesListWithoutHashes))
        filesDeletionsArray = sorted(filesDeletionsArray)

        print(INFO + " " + str(len(filesDeletionsArray)) + " files deletions were detected:")
        currentIndexDeletionsArray = 0
        for i in filesDeletionsArray:
            currentIndexDeletionsArray +=1
            print(BOLD + "[ " + OKYELLOW + str(currentIndexDeletionsArray) + '/' + str(len(filesDeletionsArray)) + ENDC + " ] " + ENDC + i)
        print("")

        # REMOVING THE ITEMS PRESENT IN THE filesDeletionsArray INTO oldFilesListWithHashes
        temp = []
        for item in oldFilesListWithHashes:
            if item[66:] not in filesDeletionsArray:
                temp.append(item)
        newFilesListWithHashes = temp
        temp = []

        # COMPARING ARRAYS oldFilesListWithoutHashes and newFilesListWithoutHashes TO FIND OUT WHICH FILES WERE ADDED
        filesAdditionsArray = list(set(newFilesListWithoutHashes) - set(oldFilesListWithoutHashes))
        filesAdditionsArray = sorted(filesAdditionsArray)

        print(INFO + " " + str(len(filesAdditionsArray)) + " new files were detected:")

        # CHECKSUMING HASHES OF filesAdditionsArray ITEMS
        filesAdditionsArray = Checksum.sha2(filesAdditionsArray)

        # JOINING newFilesListWithHashes AND filesAdditionsArray
        newFilesListWithHashes = newFilesListWithHashes + filesAdditionsArray
        newFilesListWithHashes = sorted(newFilesListWithHashes, key=lambda x:x[66:])

        return newFilesListWithHashes