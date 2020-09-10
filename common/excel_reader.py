import common.log as Log

import os
from xml.etree import ElementTree as ET
from xlrd import open_workbook
from common.config_reader import ROOT_PATH

TEST_FILE = os.path.join(ROOT_PATH,"testFile")
print(ROOT_PATH)
class dataReader():
    logger = Log.Log().get_log()

#---------------获取Excel中的测试用例数据-------------------
    #获取不同excel的内容/以及不同页签内的内容
    def get_excel(self,xls_name,sheet_name):

        self.cls = []
        self.xls_path = os.path.join(TEST_FILE,'case',xls_name)
        self.file = open_workbook(filename=self.xls_path)

        self.sheet = self.file.sheet_by_name(sheet_name=sheet_name)#获取某个sheet的内容
        self.nrow = self.sheet.nrows    #excel的行数
        for i in range(self.nrow):
            if self.sheet.row_values(i)[0]!=u'id':         #获取某一行的第一列的值
                self.cls.append(self.sheet.row_values(i))         #将每一行的值加载到一个列表返回，每一行是一个列表
        return self.cls      #返回每一行的值，并且以列表形式


# 往Excel中写入数据

#----------------获取数据库文件--------------------
    #获取XML中的值
    def set_xml(self):
        self.database = {}
        self.table = {}
        self.sql = {}
        self.sql_path = os.path.join(TEST_FILE,'SQL.xml')
        if not self.database:
            self.tree = ET.parse(self.sql_path)

            for db in self.tree.findall("database"):
                db_name = db.get("name")
                #print(db_name)
                for tb in db.findall("table"):
                    tb_name = tb.get("name")
                    #print(tb_name)
                    for data in tb.findall("sql"):
                        sql_id = data.get("id")
                        #print(sql_id)
                        #print(data.text)
                        self.sql[sql_id] = data.text.replace('\n',"").strip(" ")
                #print(self.sql)
                self.table[tb_name] = self.sql
            #print(self.table)
            self.database[db_name] = self.table
        #print(self.database)
    def get_xml_dict(self,database_name,table_name):
        self.set_xml()
        self.database_dict = self.database.get(database_name).get(table_name)
        return self.database_dict
    def get_sql(self,database_name,table_name,sql_id):
        self.db = self.get_xml_dict(database_name,table_name)
        self.sql = self.db.get(sql_id)
        return self.sql

#----------读取URL----------
    def get_xml_url(self,name):
        self.url_list = []
        self.url_data_path = os.path.join(TEST_FILE,"interfaceURL.xml")
        if not self.url_list:
            self.tree = ET.parse(self.url_data_path).getroot()
            for u in self.tree.findall("url"):
                self.url_name = u.get('name')
                #print(self.url_name)
                if self.url_name == name:
                    for c in u.getchildren():
                        self.url_list.append(c.text)
                    #print(self.url_list)
        self.url = "/"+'/'.join(self.url_list)
        #print(self.url)
        return self.url

                    #print("-------",self.url_name.)




if __name__ == '__main__':
    datared = dataReader()
    execlcontent = datared.get_excel("user.xlsx",'login')
    print("excel文件内容",execlcontent)

    database = datared.get_xml_dict('test','testtable')
    sql = datared.get_sql('test','testtable','select_member')
    print(database)
    print(sql)
    datared.get_xml_url("login")


