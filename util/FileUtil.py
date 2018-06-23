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


def isFileTypeMatches(fileName, types):
    for type in types:
        if (fileName.endswith(type)):
            return True
    return False


def getFileLinesCount(filePath):
    with open(filePath, mode="rb") as file:
        return len(file.readlines())


def readFilesInDirToOneFile(srcDir, dstFilePath, filterTypes):
    names = os.listdir(srcDir)
    if not os.path.isfile(dstFilePath):
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
