import json
import unittest

import requests

import LoginServer
import RandomUtils
import ResponseUtil
from AttachmentUrlSyncServer import AttachmentUrlSyncServer
from CategoryServer import CategoryServer

ENV = LoginServer.local_private_sit_16660000000()


class AttachmentUrlSyncTests(unittest.TestCase):

    def setUp(self):
        self.server = AttachmentUrlSyncServer(ENV)

    def test生成url附件同步任务(self):
        self.server.random_datas()

