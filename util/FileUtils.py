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
