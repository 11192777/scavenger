import json

import requests

token = "bearer eca87b5e-dbd2-4829-8d75-5911cbe92ff5"

# 开发 355006354336911360
# 测试 355006374733811712
taskType = "355006374733811712"

forms = '''
e-archive-4201
e-archive-4202
e-archive-4415
e-archive-4415
e-archive-4443
e-archive-4444
e-archive-4430
e-archive-4473
e-archive-4436
e-archive-4435
e-archive-4458
e-archive-4472
e-archive-4462
e-archive-4471
e-archive-4279
e-archive-4489
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
        "summary": str(result["summary"]).replace("柯彦钦", meName).replace("刘雪婷", meName),
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
            print(line.replace("\n", ""))
