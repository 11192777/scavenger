import random
import threading

import RandomUtils
from MySqlHelper import MysqlDb


def getNull():
    if random.randrange(0, 10) > 8:
        return "NULL"
    else:
        return "1"

class DataBuilder(threading.Thread):
    def __init__(self, url, token, count):
        threading.Thread.__init__(self)

    def run(self):
        db = MysqlDb(host="192.168.1.97", port=3306, user="root", passwd="admin", db="report_form")

        indexA = 1
        indexB = 1
        indexC = 1

        for i in range(10000):
            sql = 'INSERT INTO test1 (a_id, save_time, year, a_company, category, b_id, b_company, is_paper, c_id, type, size) VALUES {}'
            values = []
            for j in range(1000):
                values.append("({}, 1, 1000, 1, 5, {}, 7, TRUE, {}, 0, 11)".format(getNull(), getNull(), getNull()))
                indexA = indexA + 1
                indexB = indexB + 1
                indexC = indexC + 1
            sql = sql.format(", ".join(values))
            db.execute_db(sql)


if __name__ == '__main__':
    db = MysqlDb(host="192.168.1.97", port=3306, user="root", passwd="admin", db="report_form")

    indexA = 1
    indexB = 1
    indexC = 1

    for i in range(10000):
        sql = 'INSERT INTO test1 (a_id, save_time, year, a_company, category, b_id, b_company, is_paper, c_id, type, size) VALUES {}'
        values = []
        for j in range(1000):
            values.append("({}, 1, 1000, 1, 5, {}, 7, TRUE, {}, 0, 11)".format(getNull(), getNull(), getNull()))
            indexA = indexA + 1
            indexB = indexB + 1
            indexC = indexC + 1
        sql = sql.format(", ".join(values))
        db.execute_db(sql)
