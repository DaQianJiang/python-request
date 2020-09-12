import unittest
import paramunittest
from common.log import Log
from common.httpMethod import httpConfig
import ddt
import os
from common.excel_reader import dataReader
from common.commonMethod import commonMethod
import json

#获取Excel表中的测试用例
login_excel = dataReader().get_excel("user.xls",'login')
max_cols = dataReader().base_excel("user.xls",'login').ncols
httpCongigInfo = httpConfig()
commethod = commonMethod()


@paramunittest.parametrized(*login_excel)
class testLogin(unittest.TestCase):


    def setUp(self):
        self.logger = Log().get_log()
        print(self.case_name+"----测试开始----")
        #self.logger.info("---测试开始----")

    #获取Excel对应的数据，可以循环读取
    def setParameters(self,id,name,description,isExec,url,method,token,paramData,expectedResData,ruleResData,trueResDate,result):
        self.id = id
        self.name = name
        self.description = description
        self.isExec = isExec
        self.url = url
        self.method = method
        self.token = token
        self.paramData = paramData
        self.expectedResData = expectedResData
        self.ruleResData = ruleResData
        self.trueResDate = trueResDate
        self.result = result


    def test_Login(self):
        #从interfaceURL.xml中获取login的path
        #self.path = dataReader().get_xml_url("login")
        #httpCongigInfo.set_url(self.path)

        httpCongigInfo.set_url(self.url)

        print("获取到的路径--：",self.url)
        print("第一步:设置URL"+"----"+httpCongigInfo.url)

        #token
        if self.token == 'no':
            token = commethod.get_common_token()
        elif self.token == "yes":
            token = None
        header = {"Content-Type":"application/json","token":token}
        httpCongigInfo.set_header(header)
        print("第二步获取header",httpCongigInfo.headers)

        #data
        data = self.paramData
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

        print("第五步检查结果")
        #检查结果
        self.checkResult(self.ruleResData)




    def tearDown(self):

        print('-----结束-----')


    def checkResult(self,res_info):
        self.info = self.response.json()
        if self.assertEqual(self.response.status_code,200) and self.assertEqual(self.info['code'],json.loads(res_info)):
            self.trueResDate = self.info
            self.result = 'success'
            dataReader.write_excel("user.xls",'login',int(self.id),max_cols-2,self.info)
            dataReader.write_excel("user.xls",'login',int(self.id),max_cols-1,self.result)
        else:
            self.trueResDate = self.info
            self.result = "failed"
            dataReader.write_excel("user.xls",'login',int(self.id),max_cols-2,self.info)
            dataReader.write_excel("user.xls",'login',int(self.id),max_cols-1,self.result)


if __name__ == '__main__':
    unittest.main(verbosity=2)





