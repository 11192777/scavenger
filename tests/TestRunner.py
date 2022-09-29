import unittest

import FormTests
from HtmlTestRunner import HTMLTestRunner

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(FormTests.FormFieldTests))

if __name__ == '__main__':
    runner = HTMLTestRunner(output='./report', report_title=u'测试报告')
    runner.run(suite)
