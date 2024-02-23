import unittest

from lib.HTMLTestRunner_BAOBAO import HTMLTestRunner
from utils import RandomUtils

import tests.FormTests
import tests.ApiSyncTests
import tests.Tester

suite = unittest.TestSuite()
loader = unittest.TestLoader()
# suite.addTests(loader.loadTestsFromTestCase(tests.FormTests.ArchiveTypeTests))
# suite.addTests(loader.loadTestsFromTestCase(tests.FormTests.DocumentTypeTests))
# suite.addTests(loader.loadTestsFromTestCase(tests.FormTests.FormFieldTests))
suite.addTests(loader.loadTestsFromTestCase(tests.Tester.Tester))

if __name__ == "__main__":
    runer = HTMLTestRunner(title="API_TESTS",
                           description="宇宝宝起飞啦",
                           stream=open("./report/TestRunnerV2_{}.html".format(RandomUtils.current_time()), "wb"),
                           verbosity=2, retry=2, save_last_try=True)
    runer.run(suite)
