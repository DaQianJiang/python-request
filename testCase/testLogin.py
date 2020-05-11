import unittest
import paramunittest
from common.log import Log
from common.httpConfig import httpConfig
#import ddt
import os
from common.excel_reader import dataReader
from common.commonMethod import commonMethod
import json

#获取Excel表中的测试用例
login_excel = dataReader().get_excel("user.xlsx",'login')
httpCongigInfo = httpConfig()
commethod = commonMethod()

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
        print(self.case_name+"----测试开始----")
        #self.logger.info("---测试开始----")


    def test_Login(self):
        #从interfaceURL.xml中获取login的path
        self.path = dataReader().get_xml_url("login")
        httpCongigInfo.set_url(self.path)

        print("获取到的路径--：",self.path)
        print("第一步:设置URL"+"----"+httpCongigInfo.url)

        #token
        if self.token == '0':
            token = commethod.get_common_token()
        elif self.token == "1":
            token = None
        header = {"token":str(token)}
        httpCongigInfo.set_header(header)
        print("第二步获取header",httpCongigInfo.headers)

        #data
        data = {"mobilePhone":self.mobilePhone,"validateCode":self.validateCode}
        httpCongigInfo.set_data(data)
        httpCongigInfo.set_param(data)
        print("第三步:设置发送请求参数",httpCongigInfo.data)
        #执行请求获取 response
        if self.method == 'post':
            self.response = httpCongigInfo.post_method()
        elif self.method == 'get':
            self.response = httpCongigInfo.get_method()
        print("第四步发送请求\n\t\t请求方法",self.method)
        print("获得的response为:",self.response.json())

        #检查结果
        self.checkResult()
        print("第五步检查结果")


    def tearDown(self):
        
        return

    def checkResult(self):
        self.info = self.response.json()
        self.assertEqual(self.infop['code'],self.code)
        self.assertEqual(self.info["message"],self.message)
        return

if __name__ == '__main__':
    unittest.main(verbosity=2)





