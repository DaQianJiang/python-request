from common.log import Log
from common.httpMethod import httpConfig
import json
from common.config_reader import configReader
import requests

class commonMethod():
    logger = Log().get_log()
    config_http = configReader().get_url()
    config_token = configReader().get_token_config()

    def get_common_token(self):
        self.url = self.config_http["host"] + self.config_token['path']
        #print(self.url)
        self.data = {"user_name":self.config_token["user_name"],
                     "password":self.config_token["password"]}
        self.response = requests.post(url=self.url,data=self.data)
        self.info = self.response.json()
        self.token = self.info.get('token')
        #print("The token is %s"% (self.token))
        self.logger.info("the token is:%s"%(self.token))
        return self.token


   # def get_value_from_return_json(self,json,name1,name2):
    #    self.info = json["info"]

if __name__ == '__main__':
    co = commonMethod()
    co.get_common_token()

