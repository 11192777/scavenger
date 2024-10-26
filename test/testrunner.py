import threading
import requests

class Test(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        for i in range(100000000):
            res = requests.post('http://192.168.100.168:8000/alice/api/v1/account/owe',
                                data='{"annual":"2020","buildersId":"2","supplierId":"1","wellNum":"76897","queueId":"1","templateId":"1830624849597390849","fieldValues":[{"fieldValue":"12344","fieldId":"1830624882321350658","fieldName":"??1","isLink":false},{"fieldValue":"24","fieldId":"1830624961979572226","fieldName":"??2","isLink":false},{"fieldValue":"124","fieldId":"1830624971374813186","fieldName":"??2","isLink":false},{"fieldValue":"2424","fieldId":"1830624982376472578","fieldName":"2232","isLink":false}]}',
                                headers={'Content-Type': 'application/json',
                                         't-token': '3336fb63-c9ea-4277-8643-d317ecd481d7'})

if __name__ == '__main__':

    for i in range(300):
        test = Test()
        test.start()
