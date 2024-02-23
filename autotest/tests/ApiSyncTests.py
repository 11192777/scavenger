import json
import unittest

import requests

from server import LoginServer

ENV = LoginServer.embed_stage_166660000000()


class ApiSyncTests(unittest.TestCase):

    def setUp(self):
        self.headers = {"authorization": ENV["token"],
                        'Content-Type': 'application/json',
                        'key': 'archive-fields-manage'}

    def test_Api接口同步(self):
        # 资料号列表
        list = ["ZLA02062300010006110011"]
        # 先获取接口同步前，资料号对应的更新时间
        before = self.searchDocuments(list)
        print(before)
        # 点击接口同步按钮，拉取数据
        self.syncButton()
        # 等待2分钟
        # time.sleep(1000 * 60 * 2)
        # 接口同步后，再次获取资料号对应的更新时间
        after = self.searchDocuments(list)
        print(after)
        # 对比 before === after
        for key in before.keys():
            if before[key] != after[key]:
                print("Failed:{}".format(key))
            else:
                print("Success:{}".format(key))

    def syncButton(self):
        url = "http://stage.huilianyi.com/isg/e-archives/api/v1/schedule/job/trigger?roleType=TENANT"
        requestData = {
            "jobIdList": ["1480802977753464834", "1480864298757378050", "1480864504752230402",
                          "1514074920724078593", "1527126532522774530", "1567432982809255937",
                          "1582982939064954882", "1621040798209007617", "1663476424747618305"],
            "companyIdList": [], "isIncrement": True, "starTime": "2023-06-04 14:34:23",
            "endTime": "2023-06-05 14:34:23"}
        requests.post(url=url, data=json.dumps(requestData), headers=self.headers,
                      allow_redirects=False).json()

    def searchDocuments(self, docNumbers=[]):
        url = "http://stage.huilianyi.com/isg/e-archives/api/v2/documents/search?roleType=TENANT&page=0&size=300&export=False"
        requestData = {"companyIdList": [],
                       "isPaper": None, "extendSearch": None, "startCreatedDate": None,
                       "endCreatedDate": None, "createdByList": None, "collectionMethodList": None,
                       "startModifiedDate": None, "endModifiedDate": None,
                       "lastModifiedByList": None,
                       "sortField": {"fieldName": "lastModifiedDate", "sortRule": "DESC"},
                       "isInBox": False, "documentStatusList": ["WAIT_ARCHIVE", "WAIT_FILL"],
                       "isManual": False, "isWaitCheck": False,
                       "configurableOperatorBaseFieldList": [
                           {"fieldType": "DOCUMENT", "fieldName": "DOCUMENT_NUMBER",
                            "operator": "EQUAL",
                            "queryValueList": docNumbers}]}

        response = requests.post(url=url, data=json.dumps(requestData), headers=self.headers,
                                 allow_redirects=False).json()

        target = {}
        for res in response["result"]:
            target[res["documentNumber"]] = res["lastModifiedDate"]
        return target
