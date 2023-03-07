import json

import jsonpath
import re

if __name__ == '__main__':
    path = "/Users/oicoko/workspace/pycharm/scavenger/chore/info.log"
    lines = []
    a = 0

    pri = ''
    with open(path, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            for item in json.loads(line)[0]:
                pri = item["primaryField"]
                for att in item["attachmentList"]:
                    if "attachmentOID" not in att:
                        # if "fund.mobvista" in att["fileURL"]:
                            if "fileName" not in att:
                                continue
                            filename = att["fileName"]
                            url = att["fileURL"]
                            sql = '\'{{"attachTypeCode":"0","documentPrimaryField":"{}","fileName":"{}","fileUrl":"{}","traceId":"0000000000000"}}\''.format(pri, filename, url)
                            print(
                                "insert into `ea_attachment_sync_task`(`status`,`value`,`tenant_id`) values('AWAIT', {},'1272723726964219905');".format(sql))
                            a += 1
    print(a)


