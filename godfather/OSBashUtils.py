import os
import subprocess
import logging
import time

from utils import StringUtils

EVENT_STREAM_FORMAT = "data: {}\n\n"


def cmdExecute(cmd):
    yield f"data: ======> CMD READY TO EXECUTE:{cmd}\n\n"
    process = subprocess.Popen(args=cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while True:
        output = process.stdout.readline()
        if not output:
            break
        # Remove newline, as SSE will add a newline
        yield f"data: {output.decode('utf-8').strip()}\n\n"
    stdout, stderr = process.communicate()
    if process.returncode == 0:
        yield f"data: ======> CMD SUCCESS: {cmd}\n\n"
    else:
        raise RuntimeError(stderr.decode())


def mvnCleanInstall(f=None, settings=None, skipTests=True):
    cmd = "mvn clean install {skipTests} {settings} {f}".format(
        skipTests=skipTests and "-DskipTests" or "",
        settings=settings and f"--settings {settings}" or "",
        f=f and f"-f {f}" or ""
    )
    return cmdExecute(cmd)


def gitPull(C):
    cmd = "git {C} pull".format(C=C and f"-C {C}" or "")
    return cmdExecute(cmd)


def springRun(jar, active=None):
   cmd = "java -jar {active} {jar}".format(
       active=active and "-Dspring.profiles.active={}".format(active) or "",
       jar=jar
   )
   return cmdExecute(cmd)