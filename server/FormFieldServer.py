import base64

import requests

from ArchiveResult import ArchiveResult
from MySqlHelper import MysqlDb


class FormFieldServer:

    def __init__(self, env):
        self.headers = {
            'Authorization': env["token"],
            'Content-Type': 'application/json',
            'key': 'archive-fields-manage'
        }
        self.env_url = env["archive_url"]
        mysql = env["mysql"]
        if mysql is not None:
            self.db = MysqlDb(host=mysql["host"], port=mysql["port"], user=mysql["username"], passwd=str(base64.b64decode(mysql["password"]), "utf-8"), db=mysql["db"])

    def remove_by_id(self, field_id):
        save_form_url = self.env_url + '/api/v1/field?fieldId={}'.format(field_id)
        return ArchiveResult(requests.delete(url=save_form_url, headers=self.headers).json())

    def get_by_code_and_form_code(self, field_code, form_code):
        sql = "select eff.* from ea_form as ef INNER join ea_form_field as eff on ef.id = eff.form_id WHERE ef.code = '{}' and eff.code = '{}';".format(form_code, field_code)
        return self.db.select_one(sql)

    def list_form_fields(self, form_id):
        url = '/api/v1/fields?id={}'.format(form_id)
        res = requests.get(url=self.env_url + url, headers=self.headers).json()
        return ArchiveResult(res)
