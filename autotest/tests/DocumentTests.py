import server.LoginServer
from server.DocumentServer import DocumentServer
from server.FormFieldServer import FormFieldServer
from server.FormServer import FormServer

import unittest

from server.HermesServer import HermesServer
from utils import ResponseUtil

ENV = server.LoginServer.local_private_sit_16660000000()

if __name__ == '__main__':
    unittest.main()


class OpenDocumentTests(unittest.TestCase):

    def setUp(self):
        self.document_server = DocumentServer(ENV)
        self.hermes_server = HermesServer(ENV)
        self.form_field_server = FormFieldServer(ENV)
        self.form_server = FormServer(ENV)

    def tearDown(self):
        pass

    def test_未能解析的字段值(self):
        ResponseUtil.assert_status(self.document_server.open_save_document([self.document_server.random_open_document_data(fields=[{"fieldCode": "TEXT", "value": RandomUtils.random_str(300)}])]), "500000")
        ResponseUtil.assert_status(self.document_server.open_save_document([self.document_server.random_open_document_data(fields=[{"fieldCode": "TEXT", "value": RandomUtils.random_str(50)}])]), "0000")

    def test_文本数组元素个数限制(self):
        data = []
        for i in range(500):
            data.append("1")
        ResponseUtil.assert_status(self.document_server.open_save_document([self.document_server.random_open_document_data(fields=[{"fieldCode": "TEXT_ARRAY", "value": str.join(",", data)}])]), "500000")
        ResponseUtil.assert_status(self.document_server.open_save_document([self.document_server.random_open_document_data(fields=[{"fieldCode": "TEXT_ARRAY", "value": ""}])]), "0000")

    def test_文本数组元素单一元素长度限制(self):
        ResponseUtil.assert_status(self.document_server.open_save_document([self.document_server.random_open_document_data(fields=[{"fieldCode": "TEXT_ARRAY", "value": RandomUtils.random_str(500)}])]), "500000")
        ResponseUtil.assert_status(self.document_server.open_save_document([self.document_server.random_open_document_data(fields=[{"fieldCode": "TEXT_ARRAY", "value": RandomUtils.random_str(30)}])]), "0000")

    def test_最大值大于最小值(self):
        ResponseUtil.assert_status(self.document_server.open_save_document([self.document_server.random_open_document_data(fields=[{"fieldCode": "INTEGER", "value": "-9999999999999999999999"}])]), "500000")
        ResponseUtil.assert_status(self.document_server.open_save_document([self.document_server.random_open_document_data(fields=[{"fieldCode": "INTEGER", "value": "20"}])]), "0000")

    def test_去掉是否纸质单据的逻辑(self):
        pass;
