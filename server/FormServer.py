import json

import requests

import utils.RandomUtils
from common.ArchiveResult import ArchiveResult


class FormServer:
    def __init__(self, env):
        self.headers = {
            'Authorization': env["token"],
            'Content-Type': 'application/json',
            'key': 'archive-fields-manage'
        }
        self.env_url = env["archive_url"]

    def save_form(self, form_data):
        save_form_url = self.env_url + '/api/v1/document/type'
        res = requests.post(url=save_form_url, data=json.dumps(form_data), headers=self.headers).json()
        return ArchiveResult(res)

    def get_field_templates(self, current_business_env: str):
        field_template_url = self.env_url + '/api/v1/document/type/field/template'
        params = {'businessEnvironment': current_business_env}
        res = requests.get(url=field_template_url, params=params, headers=self.headers).json()
        return ArchiveResult(res)

    def delete_form(self, form_id):
        delete_form_url = self.env_url + '/api/v1/form'
        params = {'formId': form_id}
        res = requests.delete(url=delete_form_url, params=params, headers=self.headers).json()
        return ArchiveResult(res)

    def random_archive_form(self, business_type="ACCOUNTANT"):
        form = {"code": RandomUtils.random_time(), "name": RandomUtils.random_time(), "retentionPeriod": "100", "businessType": business_type, "isEnabled": True, "isParentType": True, "formFieldList": [], "sortNumber": 0}
        return self.save_form(form)

    def random_document_type(self, parent_id, business_type="LOAN_BILL"):
        form = {"isEnabled": True, "code": RandomUtils.random_time(), "name": RandomUtils.random_time(), "fieldTemplateId": "38", "baseIsPaper": "true", "attachCustomEnums": [], "parentId": parent_id, "isParentType": False, "formFieldList": [], "businessType": business_type, "sortNumber": 1}
        return self.save_form(form)

    def list_field_templates(self, current_business_env: str):
        params = {'businessEnvironment': current_business_env}
        res = requests.get(url=self.env_url + "/api/v1/document/type/field/template", params=params, headers=self.headers).json()
        return ArchiveResult(res)

    def list_parents(self):
        url = '/api/v1/document/type/parents'
        res = requests.get(url=self.env_url + url, headers=self.headers).json()
        return ArchiveResult(res)

    def get(self, form_id):
        url = '/api/v1/form/detail?formId={}'.format(form_id)
        res = requests.get(url=self.env_url + url, headers=self.headers).json()
        return ArchiveResult(res)

