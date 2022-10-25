import unittest

import FormTests
import HtmlTestRunner

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTests(loader.loadTestsFromTestCase(FormTests.ArchiveTypeTests))
suite.addTests(loader.loadTestsFromTestCase(FormTests.DocumentTypeTests))
suite.addTests(loader.loadTestsFromTestCase(FormTests.FormFieldTests))

if __name__ == '__main__':
    runner = HtmlTestRunner.HTMLTestRunner(output='./report', report_title=u'测试报告')
    runner.run(suite)
