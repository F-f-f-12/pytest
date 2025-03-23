import logging # 引用日志模块
import os
import time
from conf import setting
from logging.handlers import RotatingFileHandler # 按文件大小滚动备份

log_path = setting.FILE_PATH['LOG']
if not os.path.exists(log_path):  # 如果日志文件不存在，则新建一个文件
    os.mkdir(log_path)

# 定义日志名称
logfile_name = log_path + r'\test.{}.log'.format(time.strftime("%Y%m%d"))

# 封装日志
class RecordLog:
    def output_logging(self):
        # 获取logger对象
        logger = logging.getLogger(__name__)
        # 防止打印重复的log日志
        if not logger.handlers:
            logger.setLevel(setting.LOG_LEVEL) # 日志级别
            # 打印日志的格式，日志级别-时间-测试用例文件名称-行号-测试用例模块名/文件名-测试用例方法名-结果信息
            log_format = logging.Formatter(
                '%(levelname)s- %(asctime)s - %(filename)s:%(lineno)d - [%(module)s:%(funcName)s] - %(message)s')
            # 日志输出到指定文件， mode='a'：在日志文件内追加；maxBytes：控制单个日志文件的大小，单位是字节；backupCount：控制日志文件的数量
            fh = RotatingFileHandler(filename=logfile_name, mode='a', maxBytes=5242880, backupCount=7,encoding='utf-8')
            fh.setLevel(setting.LOG_LEVEL)  # 指定日志级别
            fh.setFormatter(log_format) # 指定日志打印格式
            logger.addHandler(fh)  # 再将相应的handler添加到logger

            # 将日志输出到控制台上
            sh = logging.StreamHandler()
            sh.setLevel(setting.STREAM_LOG_LEVEL)   # 指定日志级别
            sh.setFormatter(log_format) # 指定日志打印格式
            logger.addHandler(sh)
        return logger

apilog = RecordLog()
logs = apilog.output_logging()