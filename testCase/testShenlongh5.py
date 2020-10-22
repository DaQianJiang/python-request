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
test_file = "shennong.xls"
sheet_nme = 'shennongh5'
login_excel = dataReader().get_excel(test_file,sheet_nme)
max_cols = dataReader().base_excel(test_file,sheet_nme).ncols
httpCongigInfo = httpConfig()
commethod = commonMethod()
flag = 1


@ddt.ddt
class testLogin(unittest.TestCase):

    def setUp(self):
        #self.logger = Log().get_log()
        print("----测试开始----")
        #self.logger.info("---测试开始----")

    @ddt.data(*login_excel)
    def test_login(self,data):
        self.ids,self.name,self.description,self.isExec, \
        self.url,self.method,self.token,self.paramData,self.expectedResData,self.ruleResData,self.trueResDate,self.result = data
        print("exceldata:",self.paramData)
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
            if self.paramData == 'null':
                param_data = ''
            else:
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
            print("获得的response为:",self.response.json())
            print("获取接口请求status——code",self.response.status_code)
            print("获取接口请求参数信息",self.response.request.body)

            print("第五步检查结果")
            #检查结果
            self.checkResult(self.ruleResData)
        else:
            print("跳过用例%d"%int(self.ids))


    def tearDown(self):

        print('-----结束-----')

    def checkResult(self,res_info):
        self.info = self.response.json()
        if (self.response.status_code==100 and self.info['code']==json.loads(res_info)['code']):
            self.trueResDate = self.info
            self.result = 'success'
            dataReader().write_excel(test_file,sheet_nme,int(self.ids),(max_cols-2),self.response.text)
            dataReader().write_excel(test_file,sheet_nme,int(self.ids),(max_cols-1),self.result)
            print("用例通过")
        else:
            self.trueResDate = self.info
            self.result = "failed"
            dataReader().write_excel(test_file,sheet_nme,int(self.ids),(max_cols-2),self.response.text)
            dataReader().write_excel(test_file,sheet_nme,int(self.ids),(max_cols-1),self.result)
            print("用例失败")
        self.assertTrue(self.response.status_code==200 and self.info['code']==json.loads(res_info)['code'])

if __name__ == '__main__':
    unittest.main()





