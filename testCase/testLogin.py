import unittest
import paramunittest
from common.log import Log
from common.httpRequest import httpMethod
#import ddt

import os
from common.excel_reader import dataReader

login_excel = dataReader.get_excel("user.xlsx","login")

@paramunittest.parametrized(*login_excel)
class testLogin(unittest.TestCase):


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
        self.case_name

    def setUp(self):
        self.logger = Log().get_log()
        self.http_method = httpMethod().get_method()

    def test_Login(self):

        return




