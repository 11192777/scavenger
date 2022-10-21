import base64
import json

import requests
from jsonpath import jsonpath

import RandomUtils
from ArchiveResult import ArchiveResult
from MySqlHelper import MysqlDb


class AttachmentUrlSyncServer:
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


    def random_datas(self):
        resut = self.db.select("select unique_column from ea_document_1390141567512043521 WHERE unique_column IS NOT NULL LIMIT 10000")
        for id in jsonpath(resut, '$..unique_column'):
            data = {"attachTypeCode":"0","documentPrimaryField": id,"fileName":"人事档案资料清单_1662099245.xlsx","fileUrl":" https://5828537.extforms.netsuite.com/app/site/hosting/scriptlet.nl?script=379&deploy=1&compid=5828537&h=306de160c0adf472e5f6&filter=%7B%22id%22:9246565,%22accountingcontext%22:%22%22,%22userpreflanguage%22:%22zh_CN%22%7D&format=pdf_online","traceId":"00000000000"}
            sql = "INSERT INTO ea_attachment_sync_task (status, value, tenant_id) VALUES ('AWAIT', '{}', '{}')".format(json.dumps(data), "1390141567512043521")
            print(sql)
            self.db.execute_db(sql)

        resut = self.db.select("select unique_column from ea_document_1417103797560688642 WHERE unique_column IS NOT NULL LIMIT 10000")
        for id in jsonpath(resut, '$..unique_column'):
            data = {"attachTypeCode": "0", "documentPrimaryField": id, "fileName": "人事档案资料清单_1662099245.xlsx", "fileUrl": " https://5828537.extforms.netsuite.com/app/site/hosting/scriptlet.nl?script=379&deploy=1&compid=5828537&h=306de160c0adf472e5f6&filter=%7B%22id%22:9246565,%22accountingcontext%22:%22%22,%22userpreflanguage%22:%22zh_CN%22%7D&format=pdf_online", "traceId": "00000000000"}
            sql = "INSERT INTO ea_attachment_sync_task (status, value, tenant_id) VALUES ('AWAIT', '{}', '{}')".format(json.dumps(data), "1417103797560688642")
            print(sql)
            self.db.execute_db(sql)