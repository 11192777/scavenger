import unittest

import HtmlTestRunner

import tests.FormTests

suite = unittest.TestSuite()
loader = unittest.TestLoader()
# suite.addTests(loader.loadTestsFromTestCase(tests.FormTests.ArchiveTypeTests))
# suite.addTests(loader.loadTestsFromTestCase(tests.FormTests.DocumentTypeTests))
suite.addTests(loader.loadTestsFromTestCase(tests.FormTests.FormFieldTests))

if __name__ == '__main__':
    runner = HtmlTestRunner.HTMLTestRunner(output='./report', report_title=u'测试报告')
    runner.run(suite)
