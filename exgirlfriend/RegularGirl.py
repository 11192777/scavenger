import re

from utils import FileUtils

if __name__ == '__main__':
    infos = FileUtils.loadStr("PersonnelInfo")

    # 获取所有人员姓名
    print([re.findall(r'郑(.+?)', info) for info in infos])

