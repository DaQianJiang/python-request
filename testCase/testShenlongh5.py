import unittest
import paramunittest
from common.log import Log
from common.httpMethod import httpConfig
import ddt
import os
from common.excel_reader import dataReader
from common.CommonToken import commonMethod
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
    def test_shennong_order(self, data):
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
                          "Authorization": "bearereyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiIxODQwODI0OTQzNyIsImF1dGhvcml0aWVzIjpbInZpZXdHb29kc0RldGFpbCIsImxpc3RHb29kcyIsImFkZEdvb2RzIiwiZWRpdEdvb2RzIiwic3VibWl0R29vZHNBdWRpdCIsInJlbW92ZUdvb2RzIiwicHV0T25TYWxlIiwicHVsbE9mZlNoZWx2ZXMiLCJsaXN0TWVyY2hhbnRzTm90aWZpY2F0aW9uIiwiZGVsaXZlcnlTd2l0Y2giLCJlbmFibGVTdG9yZURlbGl2ZXJ5IiwiZGlzYWJsZVN0b3JlRGVsaXZlcnkiLCJsaXN0Um9sZXMiLCJ2aWV3Um9sZURldGFpbCIsImxpc3RVc2VycyIsInZpZXdVc2VyRGV0YWlsIiwiYWRkVXNlciIsImVkaXRVc2VyIiwiZGlzYWJsZVVzZXIiLCJkZWxldGVVc2VyIiwibGlzdENvdXBvbmNoYXJnZU9mZlJlY29yZHMiLCJjb3Vwb25DaGFyZ2VPZmYiLCJ2aWV3RGVsaXZlcnlNZ3QiLCJsaXN0Tm90aWNlcyJdLCJwbGF0Zm9ybSI6IjEiLCJjbGllbnRfaWQiOiJmYXJtX3Byb2R1Y3RfYXBwIiwiYXVkIjpbImRpY3Rpb25hcnkiLCJjb3Vwb25fbWFuYWdlbWVudCIsImxvZ2lzdGljc19tZ3QiLCJib3V0aXF1ZV9vcmRlciIsInNob3BfbWFuYWdlbWVudCIsImJvdXRpcXVlX2R1YmJvX3JlcGVhdGVyIiwiZ29vZHNjZW50ZXJfbWFuYWdlbWVudCIsIm5vdGlmaWNhdGlvbl9tYW5hZ2VtZW50Il0sImZ1bGxfbmFtZSI6IuiSi15fXiIsImF2YXRhcl91cmwiOm51bGwsInVzZXJfaWQiOjEyOTg1NTI2MjA1MzY4NTY1NzcsInNjb3BlIjpbInJlYWQiLCJ3cml0ZSJdLCJuZWVkX3Jlc2V0X3Bhc3N3b3JkIjp0cnVlLCJwaG9uZV9udW1iZXIiOiIxODQwODI0OTQzNyIsImV4cCI6MTYwMzkyNDQzNSwiY2F0ZWdvcnkiOjIsImp0aSI6Ijc4NmNjNjUyLTNlZmEtNGQ5MS05NTljLTZjYjkxMGZkOGU1NSIsInVzZXJuYW1lIjoiMTg0MDgyNDk0MzcifQ.eryuLPZdK7VB6VHM8g6S9vWg-5Z-0e3qU7mhu3xJtgeqFalCIVsV6Flc2jhPAoZdgCDpK1FewA-5MF8mUJaPobiP5QGoYWcKhCZTSbWXJtse-xWScQO4G6i57KtkpYNaYjVcY-D01lRbOsfyB3h9rTsGYDXn6b0DU0_opCuGccg"
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


            if self.extractData != '':
                print("需要提取的参数提取出来，并且写入下一行用例中:",self.extractData)
                addparam = {}
                for i in self.extractData:
                    print("正在提取的参数",i)
                    for k ,v  in json.loads(self.addData).items():
                        print("要匹配的参数",self.addData)
                        print("匹配参数每次读取的值",(k,v))
                        if i == v:
                            addparam[i] = self.response.json()[i]
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
