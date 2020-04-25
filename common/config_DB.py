from common.config_reader import configReader

import pymysql
from common.log import Log

class MyDB():
    database_config = configReader().get_database()
    logger = Log().get_log()
    def __init__(self):

        self.host = self.database_config['host']
        self.username = self.database_config['username']
        self.password = self.database_config['password']
        self.port = self.database_config['port']
        self.database = self.database_config['database']
        self.config = {
            'host':str(self.host),
            'user': self.username,
            'passwd':str(self.password),
            'port':int(self.port),
            'db':self.database
        }
        self.db = None
        self.cursor = None

    def connectDB(self):
        try:
            self.db = pymysql.connect(**self.config)
            self.cursor = self.db.cursor()
            self.logger.info("Connerct DB Successfully")
            print("-------Connerct DB Successfully---------")
        except ConnectionError as ex:
            self.logger.debug(str(ex))

    def excutSQL(self,sql):
        self.connectDB()
        self.cursor.execute(sql)
        self.db.commit()
        self.logger.info("-------commit successully-------")
        return self.cursor
    def get_all(self,cursor):
        value = cursor.fetchall()
        return value
    def get_one(self,cursor):
        value = cursor.fetchone()
        return value
    def closeDB(self):
        self.db.close()
        self.logger.info("Database closed")
        print("------Database closed----------")

if __name__ == '__main__':
    dbinfo = MyDB()
    dbinfo.connectDB()
    cursor = dbinfo.excutSQL("select * from user")
    print(dbinfo.get_all(cursor))
    print(dbinfo.get_one(cursor))
    dbinfo.closeDB()



