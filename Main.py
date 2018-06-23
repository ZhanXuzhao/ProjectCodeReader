from util.FileUtil import *
import configparser
import json

# read config
config = configparser.ConfigParser()
config.read("config.txt")
configDefault = config['DEFAULT']

srcDirPaths = json.loads(configDefault['srcDirPaths'])
dstFilePath = configDefault['dstFilePath']
filterTypes = json.loads(configDefault['filterTypes'])

clearFile(dstFilePath)
for srcDirPath in srcDirPaths:
    readFilesInDirToOneFile(srcDirPath, dstFilePath, filterTypes)
