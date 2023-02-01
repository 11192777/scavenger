import logging
import os
import shutil


def isExists(path):
    return os.path.exists(path)


def isNotExists(path):
    return not isExists(path)


def isFile(path):
    return os.path.isfile(path)


def isDirectory(path):
    return os.path.isdir(path)


def isLink(path):
    return isExists(path) and os.path.islink(path) or False


def lsFiles(dirPath):
    return isExists(dirPath) and isDirectory(dirPath) and [item for item in os.listdir(dirPath) if isFile("{}/{}".format(dirPath, item))] or []


def copyFile(oldFullPath, newFullPath):
    if not isExists(newFullPath):
        os.makedirs(newFullPath)
    shutil.copy(oldFullPath, newFullPath)


def getDir(item):
    index = item.rfind("/")
    return item[:index]


def loadStr(fileName, begin=None, end=None):
    filePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/static/"
    logging.info("===> load dir is: {}".format(filePath + fileName))
    with open(filePath + fileName, "r", encoding="utf-8") as file:
        lines = file.readlines()
        if begin is None and end is None:
            return "".join(lines)
        begin = begin is None and 0 or max(0, begin - 1)
        end = end is None and len(lines) or min(len(lines), end)
        return "".join(lines[begin:end])

def appendLog(fileName, text):
    filePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/log/" + fileName
    logging.info("===> log dir is: {}".format(filePath))
    f = open(filePath, "a+", encoding="utf-8")
    f.write(text + "\n")