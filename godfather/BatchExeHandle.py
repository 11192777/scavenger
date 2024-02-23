import os
from godfather import OSBashUtils
import logging


def aliceRebuild():
    try:
        homePath = os.environ.get("ALICE_HOME")
        yield from OSBashUtils.gitPull(homePath)
        yield from OSBashUtils.mvnCleanInstall(f=homePath + "/pom.xml")
        yield from OSBashUtils.springRun(jar=homePath + "/alice-start/target/alice.jar")
    except Exception as e:
        logging.error(f"Caught an exception: {e}")
        yield f"data: ======> CMD FAILED: {e.args}\n\n"


if __name__ == '__main__':
    for line in aliceRebuild():
        print(line)
