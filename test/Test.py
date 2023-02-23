import os

import socket

if __name__ == '__main__':
    print("ss{}".format(os.environ.get("STATIC_RESOURCE_DIR")))
    print(socket.gethostbyname(socket.gethostname()))
