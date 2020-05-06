import unittest
import paramunittest
from common.log import Log
from common.httpConfig import httpConfig
#import ddt
import os
from common.excel_reader import dataReader

#获取Excel表中的测试用例
login_excel = dataReader().get_excel("user.xlsx",'login')

@paramunittest.parametrized(*login_excel)
class testLogin(unittest.TestCase):

    #获取Excel对应的数据，可以循环读取
    def setParameters(self,case_name,method,token,mobilePhone,validateCode,data,code,message):
        self.case_name = case_name
        self.method = method
        self.token = token
        self.mobilePhone = mobilePhone
        self.validateCode = validateCode
        self.data = data
        self.code = code
        self.message = message

    def description(self):
        return  self.case_name

    def setUp(self):
        self.logger = Log().get_log()
        self.httpCongigInfo = httpConfig()


    def test_Login(self):
        #从interfaceURL.xml中获取login的path
        self.url = dataReader().get_xml_url("login")
        self.httpCongigInfo.set_url(self.url)

        print("第一步:设置URL"+"----"+self.url)

    def tearDown(self):
        return

    def checkResult(self):
        return

if __name__ == '__main__':
    unittest.main(verbosity=2)





