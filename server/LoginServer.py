import requests


def private_sit_16660000000():
    data = {
        "scope": "write",
        "username": "16660000000",
        "cryptType": 3,
        "password": "rQDJSwqpiVfd++UENU7LJPOvoci3Lirr6UoZeHn8Bd4QygPOeJUVdoatxAGtZuiIVo5eOLj67QLaB6uNd2dx+Lj02DTgPssVzl6nlStnccequMCLtUtFTTaNpgz/h31MEauEseGggtBFSkySZq8UPdgPRqYiBWVBl7OLvQg6aJ4=",
        "x-helios-client": "web",
        "client_id": "ArtemisWeb",
        "client_secret": "nLCnwdIhizWbykHyuZM6TpQDd7KwK9IXDK8LGsa7SOW",
        "grant_type": "password"
    }
    url = "http://archive-uat.huilianyi.com"
    res = requests.post(url=url + "/oauth/token", data=data).json()
    return {"token": "Bearer {}".format(res["access_token"]),
            "archive_url": url + "/isg/e-archives",
            "tenant_id": requests.get(url + "/api/account", headers={"Authorization": "Bearer {}".format(res["access_token"])}).json()["tenantId"],
            "hermes_url": url, "mysql": {
            "host": "hly-uatmask-polardb.mysql.polardb.rds.aliyuncs.com",
            "port": 3306,
            "username": "artemis",
            "password": "USF3MmUzcjR0NVle",
            "db": "e_archives_private"
        }}


def local_private_sit_16660000000():
    data = {
        "scope": "write",
        "username": "16660000000",
        "cryptType": 3,
        "password": "rQDJSwqpiVfd++UENU7LJPOvoci3Lirr6UoZeHn8Bd4QygPOeJUVdoatxAGtZuiIVo5eOLj67QLaB6uNd2dx+Lj02DTgPssVzl6nlStnccequMCLtUtFTTaNpgz/h31MEauEseGggtBFSkySZq8UPdgPRqYiBWVBl7OLvQg6aJ4=",
        "x-helios-client": "web",
        "client_id": "ArtemisWeb",
        "client_secret": "nLCnwdIhizWbykHyuZM6TpQDd7KwK9IXDK8LGsa7SOW",
        "grant_type": "password"
    }
    url = "http://archive-uat.huilianyi.com"
    res = requests.post(url=url + "/oauth/token", data=data).json()
    return {"token": "Bearer {}".format(res["access_token"]),
            "archive_url": "http://127.0.0.1:9091/e-archives",
            "tenant_id": requests.get(url + "/api/account", headers={"Authorization": "Bearer {}".format(res["access_token"])}).json()["tenantId"],
            "hermes_url": url, "mysql": {
            "host": "hly-uatmask-polardb.mysql.polardb.rds.aliyuncs.com",
            "port": 3306,
            "username": "artemis",
            "password": "USF3MmUzcjR0NVle",
            "db": "e_archives_private"
        }}


def local_private_sit_11192777():
    data = {
        "scope": "write",
        "username": "11192777",
        "cryptType": 3,
        "password": "LjDSu+DyVUjur+N2NWGh+9tvJaCwMvLn2HwSxufbDH1ayaK2smokC0hPOCVcNGy9hmZ6ekG1IwmoyiItlMwrAmzkqYphneeIznkbJcY46sVoumPkSwgXfq3fBWkbvfaJvKwwT41RiPdS7uuc27tWz4DWhrzTfua9mSE6FnViM54=",
        "x-helios-client": "web",
        "client_id": "ArtemisWeb",
        "client_secret": "nLCnwdIhizWbykHyuZM6TpQDd7KwK9IXDK8LGsa7SOW",
        "grant_type": "password"
    }
    url = "http://archive-uat.huilianyi.com"
    res = requests.post(url=url + "/oauth/token", data=data).json()
    return {"token": "Bearer {}".format(res["access_token"]),
            "archive_url": "http://127.0.0.1:9091/e-archives",
            "tenant_id": requests.get(url + "/api/account", headers={"Authorization": "Bearer {}".format(res["access_token"])}).json()["tenantId"],
            "hermes_url": url, "mysql": {
            "host": "hly-uatmask-polardb.mysql.polardb.rds.aliyuncs.com",
            "port": 3306,
            "username": "artemis",
            "password": "USF3MmUzcjR0NVle",
            "db": "e_archives_private"
        }}


def local_private_dev_11192777():
    data = {
        "scope": "write",
        "username": "11192777",
        "cryptType": 3,
        "password": "tGqDEDYttCbT0NVkaqLKu8tUPNZyGgVDWT1RQ5x0CAcSRajj5pBZ7mClhezCthVCRZBgbdGC9YjR2WIE2OjELJxPe+2ufiuqIwpTj21ZWFRXyT234OF74P/P1h+zCOlibWa4sDK73MF2uWZ+N1szT809Be+DC4kIFd9POWgt+hs=",
        "x-helios-client": "web",
        "client_id": "ArtemisWeb",
        "client_secret": "nLCnwdIhizWbykHyuZM6TpQDd7KwK9IXDK8LGsa7SOW",
        "grant_type": "password"
    }
    url = "https://archive-dev.huilianyi.com"
    res = requests.post(url=url + "/oauth/token", data=data).json()
    return {"token": "Bearer {}".format(res["access_token"]),
            "archive_url": "http://127.0.0.1:9091/e-archives",
            "tenant_id": requests.get(url + "/api/account", headers={"Authorization": "Bearer {}".format(res["access_token"])}).json()["tenantId"],
            "hermes_url": url, "mysql": {
            "host": "106.15.26.10",
            "port": 21906,
            "username": "artemis",
            "password": "MTIzNDU2TXMz",
            "db": "e_archives_jxmobile"
        }}

