from common.config_reader import configReader

import pymysql
from common.log import Log

class MyDB():

    def __init__(self):
        self.database_config = configReader().get_database()
        self.logger = Log.get_log()
        self.host = self.database_config['host']
        self.username = self.database_config['username']
        self.password = self.database_config['password']
        self.port = self.database_config['port']
        self.database = self.database_config['database']
        self.config = {
            'host':str(self.host),
            'user': self.username,
            'password':self.password,
            'port':int(self.port),
            'database':self.database
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

    def excutSQL(self):
        
