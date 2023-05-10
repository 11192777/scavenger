import datetime
import random


def random_one(list):
    return list[random.randint(0, len(list) - 1)]


def random_list(list, size):
    data = []
    for i in range(size):
        data.append(random_one(list))
    return data


def random_str(size):
    random_str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length = len(base_str) - 1
    for i in range(size):
        random_str += base_str[random.randint(0, length)]
    return random_str

def current_time():
    return random_time(par="%Y-%m-%d_%H:%M:%S")

def random_time(par="%Y_%m_%d_%H_%M_%S_%f"):
    return str(datetime.datetime.now().strftime(par))


def randomStrArray(itemLen, size):
    data = []
    for i in range(size):
        data.append(random_str(itemLen))
    return data
