import os
import re

from utils import FileUtils

hitFileSet = set()
baseDir = "/Users/vicoko/workspace/idea/sql-adapter/src/main/java/{}.java"


def buildFile(path):
    while path.find("/") > -1 and FileUtils.isNotExists(baseDir.format(path)):
        path = FileUtils.getDir(path)
    return path


def loop(startDir):
    if not FileUtils.isExists(startDir):
        return
    with open(startDir, "r", encoding="utf-8") as file:
        dirs = re.findall(r'import (.+?);', file.read())
        hitDirs = [i for i in dirs if str(i).startswith("com.alibaba")]
        hitDirPaths = [str(i).replace(".", "/") for i in hitDirs]
        rebuildPaths = []
        for path in hitDirPaths:
            if path.endswith("*"):
                files = FileUtils.lsFiles(path[:-1])
                for javaFile in files:
                    rebuildPaths.append(buildFile(path[:-1] + javaFile))
            else:
                rebuildPaths.append(buildFile(path))

        for hitDirPath in rebuildPaths:
            if hitDirPath not in hitFileSet:
                hitFileSet.add(hitDirPath)
                loop(baseDir.format(hitDirPath))


def copySingle(startDir):
    if not FileUtils.isExists(startDir):
        return
    with open(startDir, "r", encoding="utf-8") as file:
        dirs = re.findall(r'import (.+?);', file.read())
        hitDirs = [i for i in dirs if str(i).startswith("com.alibaba")]
        hitDirPaths = [str(i).replace(".", "/") for i in hitDirs]
        rebuildPaths = []
        for path in hitDirPaths:
            if path.endswith("*"):
                files = FileUtils.lsFiles(path[:-1])
                for javaFile in files:
                    rebuildPaths.append(buildFile(path[:-1] + javaFile))
            else:
                rebuildPaths.append(buildFile(path))

        for hitDirPath in rebuildPaths:
            if hitDirPath not in hitFileSet:
                hitFileSet.add(hitDirPath)
                loop(baseDir.format(hitDirPath))


if __name__ == '__main__':
    # startDir = baseDir.format("com/alibaba/druid/adapter/SqlAdapter")
    # loop(startDir)
    # for item in hitFileSet:
    #     FileUtils.copyFile(baseDir.format(item), "/desktop/{}".format(FileUtils.getDir(item)))

    copySingle("//Users/vicoko/workspace/idea/sql-adapter/src/main/java/com/alibaba/druid/sql/visitor/SQLEvalVisitorUtils.java")
    targetPath = "/Users/vicoko/workspace/idea/sql-adapter-temp/src/main/java/{}"
    for item in hitFileSet:
        print(item)
        FileUtils.copyFile(baseDir.format(item), FileUtils.getDir(targetPath.format(item)))
