import unittest

import LoginServer
from FormServer import FormServer

ENV = LoginServer.local_private_dev_11192777()


class ApiTests(unittest.TestCase):

    def setUp(self):
        self.formServer = FormServer(ENV)

    def test_新增档案类型(self):
        print(self.formServer.random_archive_form(business_type="GC").response)
