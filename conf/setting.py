import logging
import os
import sys

# 获取当前文件的根目录
DIR_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(DIR_PATH)

# log日志的输出级别
LOG_LEVEL = logging.DEBUG # 日志输出到文件
STREAM_LOG_LEVEL = logging.DEBUG # 日志输出到控制台

# 文件路径,维护为一个字典
FILE_PATH = {
    'extract' : os.path.join(DIR_PATH, 'extract.yaml'), # 字符串拼接
    'conf' : os.path.join(DIR_PATH, 'conf', 'config.ini'),
    'default_file' : os.path.join(DIR_PATH, 'testcase', 'Login', 'login_data.yaml'),
    'LOG' : os.path.join(DIR_PATH,'log')
}

print(FILE_PATH['default_file']) # 通过字典的key，获取value值