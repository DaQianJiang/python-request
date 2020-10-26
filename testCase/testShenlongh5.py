import unittest
import paramunittest
from common.log import Log
from common.httpMethod import httpConfig
import ddt
import os
from common.excel_reader import dataReader
from common.commonMethod import commonMethod
import json

# 获取Excel表中的测试用例
test_file = "shennong.xls"
sheet_nme = 'orderpayAPI'
login_excel = dataReader().get_excel(test_file, sheet_nme)
max_cols = dataReader().base_excel(test_file, sheet_nme).ncols
httpCongigInfo = httpConfig()
commethod = commonMethod()
flag = 1


@ddt.ddt
class testLogin(unittest.TestCase):

    def setUp(self):
        # self.logger = Log().get_log()
        print("----测试开始----")
        # self.logger.info("---测试开始----")

    @ddt.data(*login_excel)
    def test_login(self, data):
        self.ids, self.name, self.description, self.isExec,\
        self.url, self.method, self.token, self.paramData, self.extractData, self.addData,\
        self.expectedResData, self.validData, self.trueResDate, self.result = data

        print("exceldata:", isinstance(self.paramData,dict),self.extractData,self.addData)

        if self.isExec == 'yes':
            httpCongigInfo.set_url(self.url)
            print("第一步:设置URL" + "----" + httpCongigInfo.url)
            # token
            if self.token == 'yes':
                #token = commethod.get_common_token()

                header = {"Content-Type": "application/json",
                          "Platform": "APP",
                          "Authorization": "bearereyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVuX2lkIjoib1kwdHVzeE43ZXRyZEpwSGdmaWpMVWZxcUZPQSIsInVzZXJfbmFtZSI6IjE4NDA4MjQ5NDM3IiwiYXV0aG9yaXRpZXMiOlsidmlld0dvb2RzRGV0YWlsIiwibGlzdEdvb2RzIiwiYWRkR29vZHMiLCJlZGl0R29vZHMiLCJzdWJtaXRHb29kc0F1ZGl0IiwicmVtb3ZlR29vZHMiLCJwdXRPblNhbGUiLCJwdWxsT2ZmU2hlbHZlcyIsImxpc3RNZXJjaGFudHNOb3RpZmljYXRpb24iLCJkZWxpdmVyeVN3aXRjaCIsImVuYWJsZVN0b3JlRGVsaXZlcnkiLCJkaXNhYmxlU3RvcmVEZWxpdmVyeSIsImxpc3RSb2xlcyIsInZpZXdSb2xlRGV0YWlsIiwibGlzdFVzZXJzIiwidmlld1VzZXJEZXRhaWwiLCJhZGRVc2VyIiwiZWRpdFVzZXIiLCJkaXNhYmxlVXNlciIsImRlbGV0ZVVzZXIiLCJsaXN0Q291cG9uY2hhcmdlT2ZmUmVjb3JkcyIsImNvdXBvbkNoYXJnZU9mZiIsInZpZXdEZWxpdmVyeU1ndCIsImxpc3ROb3RpY2VzIl0sInBsYXRmb3JtIjoiMSIsImNsaWVudF9pZCI6ImZhcm1fcHJvZHVjdF9hcHAiLCJhdWQiOlsiZGljdGlvbmFyeSIsImNvdXBvbl9tYW5hZ2VtZW50IiwibG9naXN0aWNzX21ndCIsImJvdXRpcXVlX29yZGVyIiwic2hvcF9tYW5hZ2VtZW50IiwiYm91dGlxdWVfZHViYm9fcmVwZWF0ZXIiLCJnb29kc2NlbnRlcl9tYW5hZ2VtZW50Iiwibm90aWZpY2F0aW9uX21hbmFnZW1lbnQiXSwiZnVsbF9uYW1lIjoi6JKLXl9eIiwiYXZhdGFyX3VybCI6bnVsbCwidXNlcl9pZCI6MTI5ODU1MjYyMDUzNjg1NjU3Nywic2NvcGUiOlsicmVhZCIsIndyaXRlIl0sIm5lZWRfcmVzZXRfcGFzc3dvcmQiOnRydWUsInBob25lX251bWJlciI6IjE4NDA4MjQ5NDM3IiwiZXhwIjoxNjAzNzUzMjE3LCJjYXRlZ29yeSI6MiwianRpIjoiZTM0NjFhMzItNjlhNC00N2ZkLWE2MTItMDlkZDVmZWQ5MzJkIiwidXNlcm5hbWUiOiIxODQwODI0OTQzNyJ9.VCAunzXc9_xkuSP8VFtFJ7Gr2XxYU1E8JnL-SPoGgCqfE8chFkXKCy5ODwm-1uQGZcbTvbTJFuaBxMLOPBD26oA8pEH9IcNJhxHgwVcOiBc8iA9tLrH42Mg3B0AaaHE4bbhY6GLvNnj5f3ZPkpZfVr-utNyERuo-w5Va6VA7ae8"
                          }
            elif self.token == "no":
                header = {"Content-Type": "application/json"}
            httpCongigInfo.set_header(header)
            print("第二步获取header", httpCongigInfo.headers)

            # data
            if self.paramData == '':
                param_data = ''
            else:
                param_data = json.loads(self.paramData)


            if self.addData != '' and isinstance(self.addData,dict):
                print("将提取出来的参数添加到下一个参数变量中")
                dict(param_data).update(self.addData)

            httpCongigInfo.set_data(param_data)
            httpCongigInfo.set_param(param_data)
            print("第三步:设置发送请求参数", httpCongigInfo.data)

            # 执行请求获取 response
            if self.method == "post":
                self.response = httpCongigInfo.post_method()
            elif self.method == "get":
                self.response = httpCongigInfo.get_method()
            print("第四步发送请求\n\t\t请求方法", self.method)
            print("获得的response为:", self.response.json())
            print("获取接口请求status——code", self.response.status_code)
            print("获取接口请求参数信息", self.response.request.body)

            print("需要提取的参数提取出来，并且写入下一行用例中")
            if self.extractData != '':
                addparam = {}
                for i in self.extractData:
                    addparam[i] = self.response.json()['data'][i]
                dataReader().write_excel(test_file, sheet_nme, int(self.ids+1), (max_cols - 5), addparam)


            print("第五步检查结果")
            # 检查结果
            self.checkResult(self.validData)
        else:
            print("跳过用例%d" % int(self.ids))

    def tearDown(self):

        print('-----结束-----')

    def checkResult(self, res_info):
        self.info = self.response.json()
        #if (self.response.status_code == 200 and self.info['code'] == json.loads(res_info)['code']):
        if (self.response.status_code == 200 and self.info['code'] == json.loads(res_info)['code']):
            self.trueResDate = self.info
            self.result = 'success'
            dataReader().write_excel(test_file, sheet_nme, int(self.ids), (max_cols - 2), self.response.text)
            dataReader().write_excel(test_file, sheet_nme, int(self.ids), (max_cols - 1), self.result)
            print("用例通过")
        else:
            self.trueResDate = self.info
            self.result = "failed"
            dataReader().write_excel(test_file, sheet_nme, int(self.ids), (max_cols - 2), self.response.text)
            dataReader().write_excel(test_file, sheet_nme, int(self.ids), (max_cols - 1), self.result)
            print("用例失败")
        self.assertTrue(self.response.status_code == 200 and self.info['code'] == json.loads(res_info)['code'])


if __name__ == '__main__':
    unittest.main()
