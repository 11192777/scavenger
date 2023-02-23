import json
import logging
import os
import socket
import uuid

import requests

from config.setting import STATIC_RESOURCE_DIR


def noticeFeishu(content):
    logging.info("===> Notice url is:[{}]".format(content))
    data = {
        "msg_type": "post",
        "content": {
            "post": {
                "zh_cn": {
                    "title": "附件通知",
                    "content": [
                        [{
                            "tag": "text",
                            "text": "收到一个新的附件: "
                        },
                            {
                                "tag": "a",
                                "text": "请查看",
                                "href": content
                            }
                        ]
                    ]
                }
            }
        }
    }
    requests.post("https://open.feishu.cn/open-apis/bot/v2/hook/4609eee3-9e69-4140-849a-31a4a6e7d550", data=json.dumps(data))


def save(file):
    randomPath = uuid.uuid1()
    savePath = "{}/{}".format(STATIC_RESOURCE_DIR, randomPath)
    logging.info("===> Save dir is:[{}]".format(savePath))
    os.makedirs(savePath)
    logging.info("===> Dir build success.")
    fullFilePath = "{}/{}".format(savePath, file.filename)
    logging.info("===> Full file path is:[{}]".format(fullFilePath))
    file.save(fullFilePath)

    # host = socket.gethostbyname(socket.gethostname())
    host = "192.168.1.104"
    port = 8080
    noticeFeishu("http://{}:{}/{}/{}/{}".format(host, port, "files", randomPath, file.filename))
