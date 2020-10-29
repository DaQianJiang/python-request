import unittest
import paramunittest
from common.log import Log
from common.httpMethod import httpConfig
import ddt
import os
from common.excel_reader import dataReader
from common.CommonToken import commonMethod
import json
from common.casePara import casePara
from common.validM import Validation
from common.validM import AssertType

# 获取文件中的测试用例
ROOT_PATH = os.path.dirname(os.path.abspath('.'))
CONFIG_PATH = os.path.join(ROOT_PATH,'config/shennong-order.yml')
testcase = casePara(CONFIG_PATH).get_testcase()
config = casePara(CONFIG_PATH).get_config()


HOST = config["base_url"]
httpCongigInfo = httpConfig()
@ddt.ddt
class testLogin(AssertType):
    ids = 0

    def setUp(self):
        print("----测试开始----")

    @ddt.data(*testcase)
    def test_shennong_order(self, data):
        self.ids+=1
        print(data['request']['url'])
        if data['isExec']:
            httpCongigInfo.set_url(data['request']['url'])
            print("第一步:设置URL" + "----" + httpCongigInfo.url)
            if data['token']:
                header = data['request']['header']
                header['Au']='123'
            else:
                header = data['request']['header']
            httpCongigInfo.set_header(header)
            print("第二步获取header", httpCongigInfo.headers)

            if data['request']['params']=='':
                param_data = ""
            else:
                param_data = data['request']['params']
            httpCongigInfo.set_param(param_data)
            httpCongigInfo.set_data(param_data)
            print("第三步:设置发送请求参数", param_data)

            if data['request']['method']=='GET':
                self.response = httpCongigInfo.get_method()
            if data['request']['method']=='POST':
                self.response = httpCongigInfo.post_method()
            print("第四步发送请求方法", data['request']['method'])
            print("获得的response为:", self.response.json())
            print("获取接口请求status——code", self.response.status_code)
            print("获取接口请求参数信息", self.response.request.body)

            if 'validate' in data:
                for i in data['validate']:
                    valid_data = Validation().get_valid_value(i,self.response)
                    compare = Validation().get_uniform_compare(valid_data['assert'])
                    if compare=='equal':
                        assert_string = valid_data['check']
                        assert_data = valid_data['expect']
                        respondata = self.response.json()[assert_string]
                        AssertType.assert_equal_new(assert_data,respondata)
        else:
            print("跳过用例%d,%s"%(self.ids,data['name']))











    #
    #         if self.extractData != '':
    #             print("需要提取的参数提取出来，并且写入下一行用例中:",self.extractData)
    #             addparam = {}
    #             for i in self.extractData:
    #                 print("正在提取的参数",i)
    #                 for k ,v  in json.loads(self.addData).items():
    #                     print("要匹配的参数",self.addData)
    #                     print("匹配参数每次读取的值",(k,v))
    #                     if i == v:
    #                         addparam[i] = self.response.json()[i]
    #             dataReader().write_excel(test_file, sheet_nme, int(self.ids+1), (max_cols - 5), addparam)
    #
    #         print("第五步检查结果")
    #         # 检查结果
    #         self.checkResult(self.validData)
    #     else:
    #         print("跳过用例%d" % int(self.ids))
    #
    # def tearDown(self):
    #
    #     print('-----结束-----')
    #
    # def checkResult(self, res_info):
    #     self.info = self.response.json()
    #     #if (self.response.status_code == 200 and self.info['code'] == json.loads(res_info)['code']):
    #     if (self.response.status_code == 200 and self.info['code'] == json.loads(res_info)['code']):
    #         self.trueResDate = self.info
    #         self.result = 'success'
    #         dataReader().write_excel(test_file, sheet_nme, int(self.ids), (max_cols - 2), self.response.text)
    #         dataReader().write_excel(test_file, sheet_nme, int(self.ids), (max_cols - 1), self.result)
    #         print("用例通过")
    #     else:
    #         self.trueResDate = self.info
    #         self.result = "failed"
    #         dataReader().write_excel(test_file, sheet_nme, int(self.ids), (max_cols - 2), self.response.text)
    #         dataReader().write_excel(test_file, sheet_nme, int(self.ids), (max_cols - 1), self.result)
    #         print("用例失败")
    #     self.assertTrue(self.response.status_code == 200 and self.info['code'] == json.loads(res_info)['code'])
    #

if __name__ == '__main__':
    unittest.main()
