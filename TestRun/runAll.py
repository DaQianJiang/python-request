import os
import unittest
#from common.log import Log
#from common.Email import Email
from common.HTMLTestRunner import HTMLTestRunner
#from common.config_reader import configReader
from common.config_reader import ROOT_PATH
#from testCase import testLogin

report_path = os.path.join(ROOT_PATH,'testReport/report.html')
case_path = os.path.join(ROOT_PATH,"testCase")
print(case_path)


class testAll():

    def __init__(self):
        print("report_path",report_path)
       # self.config_email = configReader().get_email()
       # self.logger = Log().get_log()
       # self.email = Email()
       # self.on_off = self.config_email["on_off"]

    def run(self):
        #添加测试套件
        print("创建测试套件")
        #test_suit = unittest.TestSuite()
        #loader = unittest.TestLoader()
        test_suit = unittest.TestLoader().discover(case_path)
        #创建测试报告文件
        print("生成测试报告")
        try:
            fp = open(report_path,"wb")
            runner = HTMLTestRunner(stream=fp,verbosity=2,
                                    title="测试报告",description="登陆接口")
            runner.run(test_suit)
        except:
            raise FileNotFoundError

if __name__ == '__main__':
    test = testAll()
    test.run()


