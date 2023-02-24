import json
import logging
import re
import time
from itertools import groupby

from server.FormServer import FormServer
from utils import FileUtils, RandomUtils


class WorkTicketServer:
    apiSelector = ["文本扩容", "文本数组扩容"]

    def __init__(self, content: str, operator):
        self.content = json.loads(content)
        self.operator = operator
        self.lastModifyDate = time.strftime("-%Y%m%d", time.localtime())
        self.formCodes = ", ".join(["'{}'".format(str(item).replace(" ", "")) for item in re.split(r'[,，|?？]', self.content["formCodes"])])
        self.fieldCodes = ", ".join(["'{}'".format(str(item).replace(" ", "")) for item in re.split(r'[,，|?？]', self.content["fieldCodes"])])
        self.tenantId = self.content["tenantId"]

    def execute(self):
        target = {}
        if self.operator == "文本扩容":
            if self.content["wordsLimit"] != '':
                target["WORDS_LIMIT"] = self.content["wordsLimit"]
            if self.content["wordsMaxLimit"] != '':
                target["MAX_WORDS_LIMIT"] = self.content["wordsMaxLimit"]
        elif self.operator == "文本数组扩容":
            if self.content["wordsLimit"] != '':
                target["ITEM_WORDS_LIMIT"] = self.content["wordsLimit"]
            if self.content["wordsMaxLimit"] != '':
                target["MAX_ITEM_WORDS_LIMIT"] = self.content["wordsMaxLimit"]
            if self.content["itemLimit"] != '':
                target["ITEMS_LIMIT"] = self.content["itemLimit"]
            if self.content["itemMaxLimit"] != '':
                target["MAX_ITEMS_LIMIT"] = self.content["itemMaxLimit"]
        return self.generate(target)

    def generate(self, widgetTypeProperty):
        properties = str({key: value for key, value in widgetTypeProperty.items() if value is not None}).replace(" ", "").replace("'", '"')
        selectSql = FileUtils.loadStr("WorkTicketFormat", 13, 21).format(self.tenantId, self.formCodes, self.fieldCodes)
        updateSql = FileUtils.loadStr("WorkTicketFormat", 1, 10).format(self.lastModifyDate, properties, self.tenantId, self.formCodes, self.fieldCodes)
        FileUtils.appendLog("WorkTicketLog", time.strftime("==========> %Y-%m-%d %H:%M:%S\n", time.localtime()) + updateSql + "\n<==========\n\n")
        return "{}\n\n\n\n\n{}".format(selectSql, updateSql)


if __name__ == '__main__':
    wo = WorkTicketServer('''{"wordsLimit":"","wordsMaxLimit":"","itemLimit":"800","itemMaxLimit":"800","tenantId":"1178518358079496194","formCodes":"SA_INVOICE,SA_INVOICE,SA_INVOICE ","fieldCodes":"L_serial_no"}''', "文本数组扩容")
    print(wo.execute())
