import threading
import uuid

import LoginServer
import RandomUtils
from DocumentServer import DocumentServer

ENV = LoginServer.local_private_sit_16660000000()


class Test(threading.Thread):
    def __init__(self):
        self.documentServer = DocumentServer(ENV)
        threading.Thread.__init__(self)

    def run(self):
        keys = RandomUtils.randomStrArray(5, 10)
        for i in range(1000):
            data = {
                "companyCode": "0001",
                "documentTypeCode": "4501",
                "originalNumber": str(uuid.uuid1()),
                "isPaper": "true",
                "primaryField": RandomUtils.random_one(keys),
                "fieldValueList": [
                    {
                        "fieldCode": "TEXT_ARRAY",
                        "value": ",".join(RandomUtils.randomStrArray(100, 2000))
                    }
                ]
            }
            self.documentServer.open_save_document([data])


if __name__ == '__main__':

    for i in range(30):
        test = Test()
        test.start()
