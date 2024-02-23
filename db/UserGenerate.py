import threading
from utils import MySqlHelper
from utils import RandomUtils
import random

db = MySqlHelper.MysqlDb("127.0.0.1", 3306, "root", "isqingyu", "sachima")


def task():
    streets = ["Main Street", "Park Avenue", "Oak Street", "Maple Avenue", "Cedar Lane"]
    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
    states = ["NY", "CA", "IL", "TX", "AZ"]
    postcodes = ["10001", "90001", "60601", "77001", "85001"]

    addresses = []

    for _ in range(10000):
        street = random.choice(streets)
        city = random.choice(cities)
        state = random.choice(states)
        postcode = random.choice(postcodes)

        address = f"{street}, {city}, {state} {postcode}"
        addresses.append(address)


    prefixes = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139",
                "150", "151", "152", "153", "155", "156", "157", "158", "159",
                "170", "171", "172", "173", "175", "176", "177", "178",
                "180", "181", "182", "183", "184", "185", "186", "187", "188", "189"]

    first_names = ["John", "Jane", "Michael", "Emily", "William", "Olivia", "James", "Sophia", "Benjamin", "Isabella",
                   "Liam", "Mia", "Alexander", "Charlotte", "Daniel", "Amelia", "Henry", "Harper", "Jacob", "Evelyn"]

    last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor",
                  "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez",
                  "Robinson"]

    for i in range(10000000):

        sql = '''INSERT INTO ts_user (
                name, 
                age, 
                gender, 
                address, 
                phone_number, 
                id_card_number, 
                features, 
                gmt_time) VALUES'''
        for j in range(1000):
            prefix = random.choice(prefixes)
            number = "".join(random.choice("0123456789") for _ in range(8))
            phone_number = prefix + number
            first_name = random.choice(first_names)
            last_name = random.choice(last_names)

            sql = sql + ''' ("{}", {}, "{}", "{}", "{}", "{}", "{}", "{}")'''.format(
                f"{first_name} {last_name}",
                random.randint(1, 100),
                RandomUtils.random_one(["男", "女", "未知"]),
                RandomUtils.random_one(addresses),
                phone_number,
                random.randint(1, 999999999999) + 10000000000000,
                RandomUtils.random_str(1500),
                RandomUtils.random_time("%Y-%m-%d %H:%M:%S")
            )
            if j < 999:
                sql = sql + ","
        db.execute_db(sql)



if __name__ == '__main__':
    threads = []
    for _ in range(20):
        t = threading.Thread(target=task)
        t.start()
        threads.append(t)

    # 等待所有线程完成
    for t in threads:
        t.join()


