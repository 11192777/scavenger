import logging
import os
import sys

# 项目根路径
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_PATH)
sys.path.insert(0, BASE_PATH)  # 将项目根路径临时加入环境变量，程序退出后失效

from config.setting import SERVER_PORT

from api.apis import app

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s', datefmt='%Y-%m-%d %,H:%M:%S ', level=logging.INFO)
    # host为主机ip地址，port指定访问端口号，debug=True设置调试模式打开
    app.run(host='0.0.0.0', port=SERVER_PORT, debug=True)
