from util.FileUtil import *

srcName = "index"
matches = isFileTypeMatches(srcName, [".xml", ".java", ".kt"])
print(matches)
