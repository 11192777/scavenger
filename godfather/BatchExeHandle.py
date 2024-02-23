import os
from godfather import OSBashUtils
import logging


def aliceRebuild():
    try:
        homePath = os.environ.get("ALICE_HOME")
        pid = OSBashUtils.getPid("7077")
        if pid["pid"]:
            print("PID INFO: " + str(pid["pid"]))
            yield "data: ======> {}\n\n".format(pid["INFO"])
            yield "data: ======> {}\n\n".format(OSBashUtils.killProcess(int(pid["pid"])))
        yield from OSBashUtils.gitPull(homePath)
        yield from OSBashUtils.mvnCleanInstall(f=homePath + "/alice-start/pom.xml")
        yield from OSBashUtils.springRun(jar=homePath + "/alice-start/target/alice.jar", active="ganquan-release")
    except Exception as e:
        logging.error(f"Caught an exception: {e}")
        yield f"data: ======> CMD FAILED: {e.args}\n\n"


if __name__ == '__main__':
    aliceRebuild()