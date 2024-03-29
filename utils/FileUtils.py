import logging
import os
import shutil


def isExists(path):
    return os.path.exists(path)


def isNotExists(path):
    return not isExists(path)


def isFile(path):
    return os.path.isfile(path)


def isDirectory(path):
    return os.path.isdir(path)


def isLink(path):
    return isExists(path) and os.path.islink(path) or False


def lsFiles(dirPath):
    return isExists(dirPath) and isDirectory(dirPath) and [item for item in os.listdir(dirPath) if isFile("{}/{}".format(dirPath, item))] or []


def copyFile(oldFullPath, newFullPath):
    if not isExists(newFullPath):
        os.makedirs(newFullPath)
    shutil.copy(oldFullPath, newFullPath)


def getDir(item):
    index = item.rfind("/")
    return item[:index]


def loadStr(fileName, begin=None, end=None):
    filePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/static/"
    logging.info("===> load dir is: {}".format(filePath + fileName))
    with open(filePath + fileName, "r", encoding="utf-8") as file:
        lines = file.readlines()
        if begin is None and end is None:
            return "".join(lines)
        begin = begin is None and 0 or max(0, begin - 1)
        end = end is None and len(lines) or min(len(lines), end)
        return "".join(lines[begin:end])

def appendLog(fileName, text):
    filePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/log/" + fileName
    logging.info("===> log dir is: {}".format(filePath))
    f = open(filePath, "a+", encoding="utf-8")
    f.write(text + "\n")


# import os
# import sys
#
# from typing import Callable, List, NoReturn
#
# import pyinotify
#
# multi_event = pyinotify.IN_MODIFY | pyinotify.IN_MOVE_SELF  # 监控多个事件
#
#
# class InotifyEventHandler(pyinotify.ProcessEvent):  # 定制化事件处理类，注意继承
#     """
#     执行inotify event的封装
#     """
#     f: 'open()'
#     filename: str
#     path: str
#     wm: 'pyinotify.WatchManager'
#     output: Callable
#
#     def my_init(self, **kargs):
#         """pyinotify.ProcessEvent要求不能直接继承__init__, 而是要重写my_init, 我们重写这一段并进行初始化"""
#
#         # 获取文件
#         filename: str = kargs.pop('filename')
#         if not os.path.exists(filename):
#             raise RuntimeError('Not Found filename')
#         if '/' not in filename:
#             filename = os.getcwd() + '/' + filename
#         index = filename.rfind('/')
#         if index == len(filename) - 1 or index == -1:
#             raise RuntimeError('Not a legal path')
#
#         self.f = None
#         self.filename = filename
#         self.output: Callable = kargs.pop('output')
#         self.wm = kargs.pop('wm')
#         # 只监控路径,这样就能知道文件是否移动
#         self.path = filename[:index]
#         self.wm.add_watch(self.path, multi_event)
#
#     def read_line(self):
#         """统一的输出方法"""
#         for line in self.f.readlines():
#             self.output(line)
#
#     def process_IN_MODIFY(self, event):
#         """必须为process_事件名称，event表示事件对象, 这里表示监控到文件发生变化, 进行文件读取"""
#         if event.pathname == self.filename:
#             self.read_line()
#
#     def process_IN_MOVE_SELF(self, event):
#         """必须为process_事件名称，event表示事件对象, 这里表示监控到文件发生重新打开, 进行文件读取"""
#         if event.pathname == self.filename:
#             # 检测到文件被移动重新打开文件
#             self.f.close()
#             self.f = open(self.filename)
#             self.read_line()
#
#     def __enter__(self) -> 'InotifyEventHandler':
#         self.f = open(self.filename)
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.f.close()
#
#
# class Tail(object):
#     def __init__(
#             self,
#             file_name: str,
#             output: Callable[[str], NoReturn] = sys.stdout.write,
#             interval: int = 1,
#             len_line: int = 1024
#     ):
#         self.file_name: str = file_name
#         self.output: Callable[[str], NoReturn] = output
#         self.interval: int = interval
#         self.len_line: int = len_line
#
#         wm = pyinotify.WatchManager()  # 创建WatchManager对象
#         inotify_event_handler = InotifyEventHandler(
#             **dict(filename=file_name, wm=wm, output=output)
#         )  # 实例化我们定制化后的事件处理类, 采用**dict传参数
#         wm.add_watch('/tmp', multi_event)  # 添加监控的目录，及事件
#         self.notifier = pyinotify.Notifier(wm, inotify_event_handler)  # 在notifier实例化时传入,notifier会自动执行
#         self.inotify_event_handle: 'InotifyEventHandler' = inotify_event_handler
#
#     def __call__(self, n: int = 10):
#         """通过inotify的with管理打开文件"""
#         with self.inotify_event_handle as i:
#             # 先读取指定的行数
#             self.read_last_line(i.f, n)
#             # 启用inotify的监听
#             self.notifier.loop()
#
#     def read_last_line(self, file, n):
#         read_len: int = self.len_line * n
#
#         # 获取当前结尾的游标位置
#         file.seek(0, 2)
#         now_tell: int = file.tell()
#         while True:
#             if read_len > file.tell():
#                 # 如果跳转的字符长度大于原来文件长度,那就把所有文件内容打印出来
#                 file.seek(0)
#                 last_line_list: List[str] = file.read().split('\n')[-n:]
#                 # 重新获取游标位置
#                 now_tell: int = file.tell()
#                 break
#             file.seek(-read_len, 2)
#             read_str: str = file.read(read_len)
#             cnt: int = read_str.count('\n')
#             if cnt >= n:
#                 # 如果获取的行数大于要求的行数,则获取前n行的行数
#                 last_line_list: List[str] = read_str.split('\n')[-n:]
#                 break
#             else:
#                 # 如果获取的行数小于要求的行数,则预估需要获取的行数,继续获取
#                 if cnt == 0:
#                     line_per: int = read_len
#                 else:
#                     line_per: int = int(read_len / cnt)
#                 read_len = line_per * n
#
#         for line in last_line_list:
#             self.output(line + '\n')
#         # 重置游标,确保接下来打印的数据不重复
#         file.seek(now_tell)
#
#
# if __name__ == '__main__':
#     import argparse
#
#     parser = argparse.ArgumentParser()
#     parser.add_argument("-f", "--filename")
#     parser.add_argument("-n", "--num", default=10)
#     args, unknown = parser.parse_known_args()
#     if not args.filename:
#         raise RuntimeError('filename args error')
#     Tail(args.filename)(int(args.num))
