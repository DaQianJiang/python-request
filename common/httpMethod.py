import requests
import common.config_reader as config_reader
import common.log as log
import json



class httpConfig():
    logger = log.Log().get_log()

    def __init__(self):

        self.http_config = config_reader.configReader().get_url()
        self.host = self.http_config['host']
        self.timeout = self.http_config['timeout']
        self.headers = {}
        self.param = {} #get方法的参数
        self.data = {}  #post方法的参数
        self.url = None
        self.files = {}
        #self.proxies = {"driver-taxi.vvip-u.com":"120.77.164.223:443"}

    def set_url(self,url):
        self.url = self.host + url
        #print("httpConfig++",self.url)

    def set_header(self,header):
        self.headers = header

    def set_param(self,params):
        self.param = params

    def set_data(self,datas):
        self.data = datas

    def set_files(self,files):
        self.files = files

    def get_method(self):
        if self.param == '':
            try:
                self.response = requests.get(self.url,
                                             headers = self.headers,timeout = float(self.timeout))
                return self.response
            except TimeoutError:
                self.logger.error("Time out")
                return None
        else:
            try:
                self.response = requests.get(self.url,params=self.param,
                                             headers = self.headers,timeout = float(self.timeout))
                return self.response
            except TimeoutError:
                self.logger.error("Time out")
                return None

    def post_method(self):
        try:
            self.reponse = requests.post(self.url,headers = self.headers, data=json.dumps(self.data),
                                         files=self.files,timeout = float(self.timeout))
            return self.reponse
        except TimeoutError:
            self.logger.error("Time out")
            return None


if __name__ == '__main__':
    htt = httpConfig()
    htt.set_url('/test/api/user/doLogin')
    htt.set_header({'Content-Type': 'application/json;charset=UTF-8'})
    htt.set_data({"name":"1", "password":"111111"})
    print(htt.url)
    response  = htt.post_method()
    print("-----------------------")
    print(response.text)
    print(response.json())
    print(response.request.body)