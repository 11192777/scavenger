import json
import time
from datetime import datetime

import requests


def formatTime(timeStr):
    if timeStr == '':
        return ''
    dataTime = datetime.strptime(timeStr, '%Y/%m/%d')
    return dataTime.strftime("%Y-%m-%d")


if __name__ == '__main__':
    with open("/Users/vicoko/workspace/pycharm/scavenger/chore/PersonnelInfo", "r", encoding="utf-8") as file:
        for line in file.readlines():
            items = line.split("\t")
            data = {
                "jobNumber": items[0],
                "companyCode": "H001",
                # "departmentCode": "",
                "name": items[1],
                "sex": items[2],
                "idNumber": items[3],
                "idStartTime": formatTime(items[4]),
                "idEndTime": formatTime(items[5]),
                "entryTime": formatTime(items[6]),
                "departureTime": formatTime(items[7]),
                "email": items[11],
                "phoneNumber": items[12],
                "employmentStatus": items[13],
                "highestEducation": items[14],
                "position": items[15],
                "employeeGroup": items[16],
                "employeeSubgroup": items[17],
                "workPlace": items[18],
                "maritalStatus": items[19],
                "customFieldValueList": [
                    {
                        "fieldCode": "COMPANY_TYPE",
                        "value": items[8]
                    },
                    {
                        "fieldCode": "POSITIVE_TIME",
                        "value": formatTime(items[9])
                    },
                    {
                        "fieldCode": "PERSON_SCOPE",
                        "value": items[10]
                    },
                    {
                        "fieldCode": "COMBINED_DEGREE_PROGRAM",
                        "value": items[20]
                    }
                ]
            }
            response = requests.post(url="https://console.huilianyi.com/isg/e-archives/api/open/v1/personnel/base_info",
                                     data=json.dumps(data),
                                     headers={"authorization": "Bearer 4eb59289-fde3-4017-9a7c-0bb08732f8f5",
                                              'Content-Type': 'application/json',
                                              'key': 'archive-fields-manage'})
            print(response.text)
