import hashlib

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
                print(FAIL + '[ERROR] Checksum permission error on file: ' + i + '' + ENDC)
                errorCounter +=1
                permissionErrorException = True
            if permissionErrorException == False:
                temp.append(outputSha256 + ' *' + i)
                print(BOLD + "[ " + OKGREEN + str(currentIndexfilesList) + '/' + str(filesListLenght) + ENDC + " ] " + ENDC + outputSha256 + ' *' + i)
        filesList = temp
        temp = []

        return filesList

class Integrity:
    def check(filesList, filesListWithHashTextFilePath):

        return #todo