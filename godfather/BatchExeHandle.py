import os
from godfather import OSBashUtils
import logging


def aliceRebuild():
    try:
        yield "data: ======> {}\n\n".format("<============  REBUILD  START  <============")
        homePath = os.environ.get("ALICE_HOME")
        pid = OSBashUtils.getPid("7077")
        if pid["pid"]:
            yield "data: ======> {}\n\n".format(pid["INFO"])
            yield "data: ======> {}\n\n".format(OSBashUtils.killProcess(int(pid["pid"])))
        yield from OSBashUtils.gitPull(homePath)
        yield from OSBashUtils.mvnCleanInstall(f=homePath + "/pom.xml")
        yield from OSBashUtils.springRun(jar=homePath + "/alice-start/target/alice.jar",
                                         active="ganquan-release")
    except Exception as e:
        logging.error(f"Caught an exception: {e}")
        yield f"data: ======> CMD FAILED: {e.args}\n\n"


def aliceWebRebuild():
    try:
        yield "data: ======> {}\n\n".format("<============  REBUILD  START  <============")
        homePath = os.environ.get("ALICE_WEB_HOME")
        pid = OSBashUtils.getPid("8000")
        if pid["pid"]:
            yield "data: ======> {}\n\n".format(pid["INFO"])
            yield "data: ======> {}\n\n".format(OSBashUtils.killProcess(int(pid["pid"])))
        yield from OSBashUtils.gitPull(homePath)
        yield from OSBashUtils.pnpmInstall(homePath)
        yield from OSBashUtils.pnpmStart(homePath)
    except Exception as e:
        logging.error(f"Caught an exception: {e}")
        yield f"data: ======> CMD FAILED: {e.args}\n\n"