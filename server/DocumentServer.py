import json

import jsonpath
import requests

import RandomUtils
from ArchiveResult import ArchiveResult
from FormServer import FormServer
from HermesServer import HermesServer


class DocumentServer:
    def __init__(self, env):
        self.headers = {
            'Authorization': env["token"],
            'Content-Type': 'application/json',
            'key': 'archive-fields-manage'
        }
        self.env_url = env["archive_url"]
        self.form_server = FormServer(env)
        self.hermes_server = HermesServer(env)

    def save_document(self, document):
        url = '/api/v1/documents'
        res = requests.post(url=self.env_url + url, headers=self.headers, data=json.dumps(document)).json()
        return ArchiveResult(res)

    def open_save_document(self, batch):
        url = '/open/api/v1/import/document'
        res = requests.post(url=self.env_url + url, headers=self.headers, data=json.dumps(batch)).json()
        return ArchiveResult(res)

    def random_open_document_data(self, form_code="CONTAINS_ALL_TYPE_FIELD_FORM", fields=[], company_code=None):
        if company_code is None:
            company_code = RandomUtils.random_one(jsonpath.jsonpath(self.hermes_server.list_companies(), '$..companyCode'))
        num = RandomUtils.random_str(30)
        return {"companyCode": company_code, "documentSource": "PY_AUTO_TEST", "documentTypeCode": form_code, "fieldValueList": fields, "isPaper": True, "originalNumber": num, "primaryField": num}
