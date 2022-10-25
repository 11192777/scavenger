import unittest

import LoginServer
from FormServer import FormServer

ENV = LoginServer.local_private_dev_11192777()


class ApiTests(unittest.TestCase):

    def test_addArchiveType(self):
        self.formServer = FormServer(ENV)

    