import json

import requests

from utils import FileUtils


if __name__ == '__main__':
    lines = FileUtils.loadStr("PersonnelInfo").splitlines()

    # # 获取所有人员姓名
    # print([re.findall(r'郑(.+?)', info) for info in infos])

    for line in lines:
        info = line.split("\t")
        print(info[1])
        print(info[12])
        user = {
            "profile": {
                "id": info[12],
                "firstName": "alice",
                "lastName": info[1],
            },
            "credentials": {
                "password": "isqingyu"
            }

        }
        res = requests.post(url="http://127.0.0.1:9988/hela/engine-rest/user/create", data=json.dumps(user), headers={'Content-Type': 'application/json'})
        print(res.text)