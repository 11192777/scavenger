import os
import subprocess
import logging
import time
import signal

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


def killProcess(pid):
    os.kill(pid, signal.SIGKILL)
    return f"KILL PROCESS SUCCESSFULLY: {pid}"


def getPid(port):
    cmd = os.popen("netstat -nlp | grep :%s | awk '{print $7}' | awk -F\" / \" '{ print $1 }'" % (
        port)).read()
    pid = cmd and cmd.split('/')[0] or ""
    return {"pid": f"{pid}", "INFO": f"PROCESS_INFO:{cmd}"}


def pnpmInstall(C):
    cmd = "pnpm install {C}".format(C=C and "-C {}".format(C) or "")
    return cmdExecute(cmd)


def pnpmStart(dir):
    cmd = "pnpm {dir} start".format(dir=dir and "--dir={}".format(dir) or "")
    return cmdExecute(cmd)
