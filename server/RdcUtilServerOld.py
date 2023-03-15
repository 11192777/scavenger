import json

import requests

token = "bearer 182d43de-81e0-4f59-9c4c-1052d9202e87"

# 开发 355006354336911360
# 测试 355006374733811712
taskType = 355006354336911360

forms = '''
e-archive-4521
'''


def createSub(code):
    headers = {"h-tenant-id": "1", "Authorization": token, "Content-Type": "application/json"}
    meUrl = "https://c7n-api.huilianyi.com/iam/choerodon/v1/users/self"
    me = requests.get(url=meUrl, headers=headers, allow_redirects=False).json()
    meName = me["realName"]
    search = {
        "advancedSearchArgs": {},
        "otherArgs": {
            "customField": {
                "option": [],
                "date": [],
                "date_hms": [],
                "number": [],
                "string": [],
                "text": []
            }
        },
        "searchArgs": {
            "tree": True
        },
        "contents": [
            code
        ]
    }
    searchUrl = "https://c7n-api.huilianyi.com/agile/v1/projects/172811994888671232/issues/include_sub?page=0&size=10"
    result = requests.post(url=searchUrl, data=json.dumps(search), headers=headers, allow_redirects=False).json()["content"][0]
    subTask = {
        "summary": "【{}】".format(meName) + str(result["summary"]),
        "projectId": result["projectId"],
        "priorityId": result["priorityVO"]["id"],
        "parentIssueId": result["issueId"],
        "issueTypeId": taskType,
        "typeCode": "sub_task",
        "sprintId": 0,
        "assigneeId": me["id"],
        "priorityCode": "priority-{}".format(result["priorityVO"]["id"]),
        "programId": result["projectId"],
        "epicId": 0,
        "relateIssueId": 0,
        "componentIssueRelVOList": [],
        "description": "",
        "issueLinkCreateVOList": [],
        "labelIssueRelVOList": [],
        "versionIssueRelVOList": [],
        "featureId": 0,
        "productIds": []
    }
    createSubTaskUrl = "https://c7n-api.huilianyi.com/agile/v1/projects/172811994888671232/issues/sub_issue"
    ok = requests.post(url=createSubTaskUrl, data=json.dumps(subTask), headers=headers, allow_redirects=False).json()
    print(ok)


if __name__ == '__main__':
    for line in forms.splitlines():
        if line.startswith("e-archive"):
            createSub(line)
