import common.log as Log

import os
from xml.etree import ElementTree as ET
from common.config_reader import ROOT_PATH
from xlutils.copy import copy

TEST_FILE = os.path.join(ROOT_PATH,"testFile")
print(ROOT_PATH)
class xmlReader():
    logger = Log.Log().get_log()


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
    datared = xmlReader()
    # database = datared.get_xml_dict('test','testtable')
    # sql = datared.get_sql('test','testtable','select_member')
    # print(database)
    # print(sql)
    # datared.get_xml_url("login")


