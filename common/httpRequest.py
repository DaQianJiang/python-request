import requests
import common.config_reader as config_reader
import common.log as log



class httpMethod():
    def __init__(self):
        self.logger = log.Log().get_log()
        self.http_config = config_reader.configReader().get_url()
        self.host = self.http_config['host']
        self.timeout = self.http_config['timeout']
        self.headers = {}
        self.param = {} #get方法的参数
        self.data = {}  #post方法的参数
        self.url = None
        self.files = {}

    def set_url(self,url):
        self.url = self.host + url

    def set_header(self,header):
        self.headers = header

    def set_param(self,params):
        self.param = params

    def set_data(self,datas):
        self.data = datas

    def set_files(self,files):
        self.files = files

    def get_method(self):
        try:
            self.response = requests.get(self.url,params=self.param,
                                         headers = self.headers,timeout = float(self.timeout))
            return self.response
        except TimeoutError:
            self.logger.error("Time out")
            return None

    def post_method(self):
        try:
            self.reponse = requests.post(self.url,headers = self.headers, data=self.data,
                                         files=self.files,timeout = float(self.timeout))
            return self.reponse
        except TimeoutError:
            self.logger.error("Time out")
            return None
if __name__ == '__main__':
    htt = httpMethod()
    response  = 