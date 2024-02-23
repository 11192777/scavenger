import os
from godfather import OSBashUtils
import logging


def aliceRebuild():
    try:
        homePath = os.environ.get("ALICE_HOME")
        homePath = "/Users/vance/workspace/idea/tos-seller-manager"
        yield from OSBashUtils.gitPull(homePath)
        yield from OSBashUtils.mvnCleanInstall(f=homePath + "/pom.xml", settings="/Users/vance/.m2/settings-tmall.xml")
    except Exception as e:
        logging.error(f"Caught an exception: {e}")
        yield f"data: ======> CMD FAILED: {e.args}\n\n"


if __name__ == '__main__':
    for line in aliceRebuild():
        print(line)
