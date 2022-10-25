import json

import jsonpath
import re

if __name__ == '__main__':
    path = "/Users/vicoko/workspace/pycharm/scavenger/chore/info.log"
    lines = []
    a = 0

    pri = ''
    with open(path, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            for item in json.loads(line)[0]:
                pri = item["primaryField"]
                if pri == '20221024103153624617':
                    print(item)
                for att in item["attachmentList"]:
                    if "attachmentOID" not in att:
                        if "miniso" in att["fileURL"]:
                            filename = att["fileName"]
                            url = att["fileURL"]
                            # sql = '\'{{"attachTypeCode":"0","documentPrimaryField":"{}","fileName":"{}","fileUrl":"{}","traceId":"0000000000000"}}\''.format(pri, filename, url)
                            # print(
                            #     "insert into `ea_attachment_sync_task`(`status`,`value`,`tenant_id`) values('AWAIT', {},'1194824448723337218');".format(sql))
                            a += 1
    print(a)


