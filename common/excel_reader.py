import common.log as Log

import os
from xml.etree import ElementTree as ET
from xlrd import open_workbook
from common.config_reader import ROOT_PATH
from xlutils.copy import copy

TEST_FILE = os.path.join(ROOT_PATH,"testFile")
print(ROOT_PATH)
class dataReader():
    logger = Log.Log().get_log()



#---------------获取Excel中的测试用例数据-------------------

    #excel基本操作如：打开文件，获取行数和列数
    def base_excel(self,xls_name,sheet_name):
        self.xls_path = os.path.join(TEST_FILE,'case',xls_name)
        self.file = open_workbook(filename=self.xls_path)
        self.sheet = self.file.sheet_by_name(sheet_name=sheet_name)#获取某个sheet的内容
        return self.sheet

    #获取不同excel的内容/以及不同页签内的内容
    def get_excel(self,xls_name,sheet_name):

        self.cls = []
        self.sheet = self.base_excel(xls_name,sheet_name)#获取某个sheet的内容
        self.nrow = self.sheet.nrows    #excel的行数
        for i in range(self.nrow):
            if self.sheet.row_values(i)[0]!=u'id':         #获取某一行的第一列的值
                self.cls.append(self.sheet.row_values(i))         #将每一行的值加载到一个列表返回，每一行是一个列表
        return self.cls      #返回每一行的值，并且以列表形式


# 往Excel中写入数据
    def write_excel(self,xls_name,sheet_name,row,col,value):
        self.xls_path = os.path.join(TEST_FILE,'case',xls_name)
        self.file = open_workbook(filename=self.xls_path)

        #self.data = self.base_excel(xls_name,sheet_name)
        self.data_copy = copy(self.file)
        self.sheet = self.data_copy.get_sheet(sheet=sheet_name)
        print("-----",self.data_copy)
        self.sheet.write(row, col, value)  # 在某一单元格写入value
        self.data_copy.save(self.xls_path)  # 保存文件
        print("---向Excel追加数据成功----")





if __name__ == '__main__':
    datared = dataReader()
    mm = datared.base_excel("user.xls",'login')
    execlcontent = datared.get_excel("user.xls",'login')
    print("excel文件内容",execlcontent)
    print(mm.ncols)

    #datared.write_excel("user.xls","testlearn",2,4,"success")



