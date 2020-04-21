import  logging
import os
import time
from common.config_reader import ROOT_PATH
import common.config_reader as config_reader
from logging import FileHandler
from logging import StreamHandler

LOG_PATH = os.path.join(ROOT_PATH,'log')

class Log():
    def __init__(self):
        if not os.path.exists(LOG_PATH):
            os.mkdir(LOG_PATH)
        self.config_Reader = config_reader.configReader() #创建config_reader对象
        self.config_logger = self.config_Reader.get_log()
        self.file_lever = self.config_logger['file_level']
        self.console_level = self.config_logger['console_level']
        self.format = self.config_logger['format']
        self.datefmt = self.config_logger['datefmt']

        #日志对象
        self.logger = logging.getLogger(__name__)
        #控制台输出 hander/format
        self.logger.setLevel(level=self.console_level)
        self.formatter = logging.Formatter(fmt=self.format,datefmt=self.datefmt)
        self.console_hander = StreamHandler()
        self.console_hander.setFormatter(self.formatter)
        self.logger.addHandler(self.console_hander)

        #fileHander输出
        nowday = time.strftime("%Y%m%d")
        self.filename = os.path.join(LOG_PATH,nowday+'.log')
        self.file_hander = FileHandler(self.filename)
        self.file_hander.setLevel(self.file_lever)
        self.file_hander.setFormatter(self.formatter)
        self.logger.addHandler(self.file_hander)
    def get_log(self):

        return self.logger





if __name__ == '__main__':
    c = Log()
    c.get_log().info('testtttttt')











