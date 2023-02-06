import json

import requests

from common.ArchiveResult import ArchiveResult


class CategoryServer:
    def __init__(self, env):
        self.headers = {
            'Authorization': env["token"],
            'Content-Type': 'application/json',
            'key': 'archive-fields-manage'
        }
        self.env_url = env["archive_url"]

    def listSubCategory(self, parentId=None, isEnabled=None, isWithSubCategory=None):
        url = "/api/v1/categories"
        params = {"parentId": parentId, "isEnabled": isEnabled, "isWithSubCategory": isWithSubCategory}
        res = requests.get(url=self.env_url + url, params=params, headers=self.headers).json()
        return ArchiveResult(res)

    def saveOrUpdate(self, data):
        url = "/api/v1/category"
        res = requests.post(url=self.env_url + url, data=json.dumps(data), headers=self.headers).json()
        return ArchiveResult(res)
