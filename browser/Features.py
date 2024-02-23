import json
import sys
def decode(str):
    str = str.replace('#3A', ';')
    str = str.replace('#3B', ':')
    return str
def toJson(noff):
    jsonObj = {}
    items = noff.split(';')
    for item in items:
        kv = item.split(':')
        k = decode(kv[0])
        v = decode(kv[1])
        if k is not None and k != '':
            jsonObj[k] = v
    print(json.dumps(jsonObj, sort_keys=True, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    args = sys.argv
    print(toJson(args[0]))