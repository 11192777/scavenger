import json

import requests


class StrUtilServer:
    apiSelector = [
        "Java str to py format",
        "Java class to JSON",
        "发送到飞书"
    ]

    def __init__(self, type, content):
        self.type = type
        self.content = content

    def execute(self):
        if self.type == self.apiSelector[0]:
            return self.javaStrToPyFormat()
        elif self.type == self.apiSelector[1]:
            return self.javaClassToJSON()
        elif self.type == self.apiSelector[2]:
            return self.sendToFeishu()

    def javaStrToPyFormat(self):
        data = str(self.content)
        data = data.replace("{", "{{")
        data = data.replace("}", "}}")
        return data

    def javaClassToJSON(self):
        data = str(self.content)

    def sendToFeishu(self):
        data = {
            "msg_type": "post",
            "content": {
                "post": {
                    "zh_cn": {
                        "title": "消息接受",
                        "content": [
                            [
                                {
                                    "tag": "text",
                                    "text": self.content
                                }
                            ]
                        ]
                    }
                }
            }
        }
        requests.post("https://open.feishu.cn/open-apis/bot/v2/hook/4609eee3-9e69-4140-849a-31a4a6e7d550", data=json.dumps(data))
