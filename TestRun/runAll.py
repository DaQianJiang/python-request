import os
import unittest
from common.log import Log
from common.EmailMethod import Email
from common.HTMLTestRunner import HTMLTestRunner
from common.config_reader import configReader
from common.config_reader import ROOT_PATH


report_path = os.path.join(ROOT_PATH,'testReport/report.html')

#测试用例所在文件夹
case_path = os.path.join(ROOT_PATH,"testCase")


class testAll():
    logger = Log().get_log()

    def __init__(self):
        global logger
        self.config_email = configReader().get_email()
        self.email = Email()
        self.on_off = self.config_email["on_off"]

    def run(self):
        #添加测试套件
        self.logger.info("创建测试套件")
        #将文件夹中的测试用例一起执行
        test_suit = unittest.TestLoader().discover(case_path)
        #创建测试报告文件
        self.logger.info("生成测试报告")
        try:
            self.fp = open(report_path,"wb")
            runner = HTMLTestRunner(stream=self.fp,verbosity=2,
                                    title="测试报告",description="登陆接口")
            runner.run(test_suit)
        except:
            raise FileNotFoundError
        finally:
            self.fp.close()
            if self.on_off =="1":
                self.email.send_email()
            elif self.on_off=="0":
                self.logger.info("Dont need to send Email")
            else:
                self.logger.error("unknow status")

if __name__ == '__main__':
    test = testAll()
    test.run()


