import os


def readFile(filePath, encoding='utf-8'):
    with open(filePath, encoding=encoding) as file:
        return file.readlines()


def writeFile(filePath, lines, encoding='utf-8', mode='a'):
    with open(filePath, mode=mode, encoding=encoding) as file:
        file.writelines(lines)
        file.write("\n")


def clearFile(filePath):
    with open(filePath, mode="w") as file:
        file.writelines("")


def printFile(filePath):
    with open(filePath, encoding="utf-8") as f:
        for line in f:
            print(line)


def isFileTypeMatches(fileName, types):
    for type in types:
        if (fileName.endswith(type)):
            return True
    return False


def readFilesInDirToOneFile(srcDir, dstFilePath, filterTypes):
    names = os.listdir(srcDir)
    # create file if need
    if (not os.path.isfile(dstFilePath)):
        os.makedirs(dstFilePath)
    for name in names:
        srcName = os.path.join(srcDir, name)
        if os.path.isdir(srcName):
            readFilesInDirToOneFile(srcName, dstFilePath, filterTypes)
        elif os.path.isfile(srcName):
            matches = isFileTypeMatches(srcName, filterTypes)
            if matches:
                print(srcName)
                writeFile(dstFilePath, name)
                writeFile(dstFilePath, readFile(srcName))
                writeFile(dstFilePath, "")
