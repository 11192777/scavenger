import json

import requests


class RdcUtilServer:

    def __init__(self, token):
        self.token = token
        self.headers = {"h-tenant-id": "1", "Authorization": token, "Content-Type": "application/json"}
        self.meInfo = None
        self.users = []

    def getMeInfo(self):
        if self.meInfo is not None:
            return self.meInfo
        url = "https://c7n-api.huilianyi.com/iam/choerodon/v1/users/self"
        self.meInfo = requests.get(url=url, headers=self.headers, allow_redirects=False).json()
        return self.meInfo

    def getMeName(self):
        return self.getMeInfo()["realName"]

    def queryTaskByCode(self, taskCode):
        url = "https://c7n-api.huilianyi.com/agile/v1/projects/172811994888671232/issues/include_sub?page=0&size=10"
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
                str(taskCode)
            ]
        }
        return requests.post(url=url, data=json.dumps(search), headers=self.headers, allow_redirects=False).json()["content"][0]

    def saveSubTask(self, taskCode, taskTypeName, associateName=None):
        taskInfo = self.queryTaskByCode(taskCode)
        if associateName:
            self.initMeInfoByUserName(associateName)
        taskDetail = self.getTaskDetail(taskInfo["issueId"])
        subTask = {
            "summary": "【{}】".format(self.getMeName()) + str(taskInfo["summary"]),
            "projectId": taskInfo["projectId"],
            "priorityId": taskInfo["priorityVO"]["id"],
            "parentIssueId": taskInfo["issueId"],
            "issueTypeId": self.getTaskTypeId(taskTypeName),
            "typeCode": "sub_task",
            "sprintId": 0,
            "assigneeId": self.getMeInfo()["id"],
            "priorityCode": "priority-{}".format(taskInfo["priorityVO"]["id"]),
            "programId": taskInfo["projectId"],
            "epicId": 0,
            "relateIssueId": 0,
            "componentIssueRelVOList": [],
            "description": taskDetail["description"],
            "issueLinkCreateVOList": [],
            "labelIssueRelVOList": [],
            "versionIssueRelVOList": [],
            "featureId": 0,
            "productIds": []
        }
        url = "https://c7n-api.huilianyi.com/agile/v1/projects/172811994888671232/issues/sub_issue"
        ok = requests.post(url=url, data=json.dumps(subTask), headers=self.headers, allow_redirects=False).json()
        print(ok)

    def getTaskId(self, taskCode):
        return self.queryTaskByCode(taskCode)["issueId"]

    def getTaskTypeId(self, nameFilter):
        url = "https://c7n-api.huilianyi.com/agile/v1/projects/172811994888671232/schemes/query_issue_types_with_sm_id?apply_type=agile"
        types = requests.get(url=url, headers=self.headers, allow_redirects=False).json()
        for typeItem in types:
            if typeItem["name"] == nameFilter:
                return typeItem["id"]
        return None

    def queryUser(self, userName):
        for user in self.users:
            if user["name"] == userName:
                return user["info"]
        url = "https://c7n-api.huilianyi.com/iam/choerodon/v1/projects/172811994888671232/users/agile?param={}&page=0&size=50&enabled=true".format(userName)
        userInfo = requests.post(url=url, data=json.dumps([]), headers=self.headers, allow_redirects=False).json()["content"][0]
        self.users.append({"name": userName, "info": userInfo})
        return userInfo

    def getUserIdByName(self, userName):
        user = self.queryUser(userName)
        return user is not None and user["id"] or None

    def queryTaskById(self, taskId):
        url = "https://c7n-api.huilianyi.com/agile/v1/projects/172811994888671232/project_invoke_agile/issues/{}?organizationId=1&instanceProjectId=172811994888671232".format(taskId)
        return requests.get(url=url, headers=self.headers, allow_redirects=False).json()

    def getNextTaskVersionNumber(self, taskId):
        return self.queryTaskById(taskId)["objectVersionNumber"]

    def updateTester(self, taskId, userId):
        data = {
            "fieldType": "member",
            "value": userId
        }
        url = " https://c7n-api.huilianyi.com/agile/v1/projects/172811994888671232/field_value/update/{}?organizationId=1&schemeCode=agile_issue&fieldId=128600069423116288&fieldCode=org_tester".format(taskId)
        print(requests.post(url=url, data=json.dumps(data), headers=self.headers, allow_redirects=False).json())

    def updateAssociateMember(self, taskId, version, userIds):
        data = {
            "issueId": taskId,
            "objectVersionNumber": version,
            "participantIds": userIds
        }
        url = "https://c7n-api.huilianyi.com/agile/v1/projects/172811994888671232/issues"
        print(requests.put(url=url, data=json.dumps(data), headers=self.headers, allow_redirects=False).json())

    def saveTaskAssociateMember(self, line: str):
        items = line.split()
        taskId = self.getTaskId(items[0])
        if items[3] != '-':
            self.updateTester(taskId=taskId, userId=self.getUserIdByName(items[3]))
        userIds = []
        if items[1] != '-':
            userIds.append(self.getUserIdByName(items[1]))
        if items[2] != '-':
            userIds.append(self.getUserIdByName(items[2]))
        version = self.getNextTaskVersionNumber(taskId=taskId)
        self.updateAssociateMember(taskId=taskId, version=version, userIds=userIds)

    def initMeInfoByUserName(self, associateName):
        meInfo = {
            "realName": associateName,
            "id": self.getUserIdByName(associateName)
        }
        self.meInfo = meInfo

    def getTaskDetail(self, taskId):
        url = "https://c7n-api.huilianyi.com/agile/v1/projects/172811994888671232/issues/{}?organizationId=1&instanceProjectId=172811994888671232".format(taskId)
        return requests.get(url=url, headers=self.headers, allow_redirects=False).json()
