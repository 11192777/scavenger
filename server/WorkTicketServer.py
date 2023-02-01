import json
import logging
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

    def execute(self):
        if self.operator == "文本扩容":
            return self.generate({
                "WORDS_LIMIT": self.content["wordsLimit"],
                "MAX_WORDS_LIMIT": self.content["wordsMaxLimit"]
            })
        elif self.operator == "文本数组扩容":
            return self.generate({
                "ITEM_WORDS_LIMIT": self.content["wordsLimit"],
                "MAX_ITEM_WORDS_LIMIT": self.content["wordsMaxLimit"],
                "ITEMS_LIMIT": self.content["itemLimit"],
                "MAX_ITEMS_LIMIT": self.content["itemMaxLimit"],
            })

    def generate(self, widgetTypeProperty):
        result = str({key: value for key, value in widgetTypeProperty.items() if value is not None}).replace(" ", "").replace("'", '"')
        targetSql = FileUtils.loadStr("WorkTicketFormat").format(self.lastModifyDate, result, self.content["tenantId"],
                                                            ",".join(["'{}'".format(item) for item in
                                                                      self.content["formCodes"].split(',')]),
                                                            ",".join(["'{}'".format(item) for item in
                                                                      self.content["fieldCodes"].split(',')]))
        FileUtils.appendLog("WorkTicketLog", time.strftime("==========> %Y-%m-%d %H:%M:%S\n", time.localtime()) + targetSql + "\n<==========\n\n")
        return targetSql
