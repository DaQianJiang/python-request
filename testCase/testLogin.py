import unittest
#import paramunittest
from common.log import Log
from common.httpRequest import httpMethod

import os
from common.excel_reader import dataReader

class testLogin(unittest.TestCase):
    logger = Log().get_log()
    http_method = httpMethod().get_method()
    login_excel = dataReader.get_excel("user.xlsx","login")



