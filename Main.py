from util.FileUtil import *
import configparser

# read config
config = configparser.ConfigParser()
config.read("config.txt")
configDefault = config['DEFAULT']

srcDirPath = configDefault['srcDirPath']
dstFilePath = configDefault['dstFilePath']
filterTypes = configDefault['filterTypes']

clearFile(dstFilePath)
readFilesInDirToOneFile(srcDirPath, dstFilePath, filterTypes)
