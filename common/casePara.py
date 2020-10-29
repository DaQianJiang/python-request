import yaml
import configparser
import os


ROOT_PATH = os.path.dirname(os.path.abspath('.'))
#CONFIG_PATH = os.path.join(ROOT_PATH,'config/config.yaml')

class casePara():
    def __init__(self,file_path):
        self.file_path = file_path

    def caseParas(self,element):
        if os.path.exists(self.file_path):
            with open(self.file_path,'rb') as f :
                self.caseData = yaml.safe_load(f.read()).get(element)
            return self.caseData
        else:
            raise FileNotFoundError("yml文件不存在-%s"%self.file_path)

    def get_config(self):
        self.config_value = self.caseParas('config')
        return self.config_value

    def get_testcase(self):
        self.case_value = self.caseParas("testcase")
        return self.case_value





if __name__ == '__main__':
    CONFIG_PATH = os.path.join(ROOT_PATH,'config/shennong-order.yml')
    ca = casePara(CONFIG_PATH)
    datas = ca.get_config()
    testcase = ca.get_testcase()
    for case in testcase:
        header = case['request']['header']
        #header['uu']=123
        header.update({"country": "china"})
        #print("testcase",case)
        print(case['validate'])

    #print(ca.get_valid_value()['validate'])
   # print(datas)



                
