import unittest
import paramunittest
from common.log import Log
from common.httpMethod import httpConfig
import ddt
import os
from common.excel_reader import dataReader
from common.CommonToken import commonMethod
import json


#获取Excel表中的测试用例
test_file = "user.xls"
sheet_name = 'login'
login_excel = dataReader().get_excel(test_file,sheet_name)
max_cols = dataReader().base_excel(test_file,sheet_name).ncols
httpCongigInfo = httpConfig()
commethod = commonMethod()
flag = 1


@ddt.ddt
#@paramunittest.parametrized(*login_excel)
class testLogin(unittest.TestCase):

    #获取Excel对应的数据，可以循环读取
    # def setParameters(self,ids,name,description,isExcu,url,method,token,paramData,expectedResData,ruleResData,trueResDate,result):
    #     self.ids = ids
    #     self.name = name
    #     self.description = description
    #     self.isExec = isExcu
    #     self.url = url
    #     self.method = method
    #     self.token = token
    #     self.paramData = paramData
    #     self.expectedResData = expectedResData
    #     self.ruleResData = ruleResData
    #     self.trueResDate = trueResDate
    #     self.result = result

    def setUp(self):
        #self.logger = Log().get_log()
        print("----测试开始----")
        #self.logger.info("---测试开始----")

    @ddt.data(*login_excel)
    def test_login(self,data):
        self.ids,self.name,self.description,self.isExec, \
        self.url,self.method,self.token,self.paramData,self.expectedResData,self.ruleResData,self.trueResDate,self.result = data
        #从interfaceURL.xml中获取login的path
        #self.path = dataReader().get_xml_url("login")
        #httpCongigInfo.set_url(self.path)

        if self.isExec == 'yes':
            httpCongigInfo.set_url(self.url)

            #print("获取到的路径--：",self.url)
            print("第一步:设置URL"+"----"+httpCongigInfo.url)

            #token
            if self.token == 'yes':
                token = commethod.get_common_token()
                header = {"Content-Type":"application/json","token":token}
            elif self.token == "no":
                token = None
                header = {"Content-Type":"application/json"}
            httpCongigInfo.set_header(header)
            print("第二步获取header",httpCongigInfo.headers)

            #data
            param_data = json.loads(self.paramData)
            httpCongigInfo.set_data(param_data)
            httpCongigInfo.set_param(param_data)
            print("第三步:设置发送请求参数",httpCongigInfo.data)
            #执行请求获取 response
            if self.method == "post":
                self.response = httpCongigInfo.post_method()
            elif self.method == "get":
                self.response = httpCongigInfo.get_method()
            print("第四步发送请求\n\t\t请求方法",self.method)

            print("获取接口请求status——code", self.response.status_code)
            print("获取接口请求参数信息", self.response.request.body)
            print("获得的response为:",self.response.json())

            print("第五步检查结果")
            #检查结果
            self.checkResult(self.ruleResData,test_file,sheet_name)
        else:
            print("跳过用例%d"%int(self.ids))


    def tearDown(self):

        print('-----结束-----')


    def checkResult(self,res_info,test_file,sheet_name):
        self.info = self.response.json()
        if (self.response.status_code==200 and self.info['code']==json.loads(res_info)['code']):
            self.trueResDate = self.info
            self.result = 'success'
            dataReader().write_excel(test_file,sheet_name,int(self.ids),(max_cols-2),self.response.text)
            dataReader().write_excel(test_file,sheet_name,int(self.ids),(max_cols-1),self.result)
            print("用例通过")
        else:
            self.trueResDate = self.info
            self.result = "failed"
            dataReader().write_excel(test_file,sheet_name,int(self.ids),(max_cols-2),self.response.text)
            dataReader().write_excel(test_file,sheet_name,int(self.ids),(max_cols-1),self.result)
            print("用例失败")
        self.assertTrue(self.response.status_code==200 and self.info['code']==json.loads(res_info)['code'])

if __name__ == '__main__':
    unittest.main()





