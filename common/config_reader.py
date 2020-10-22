import os
import yaml


ROOT_PATH = os.path.dirname(os.path.abspath('.'))
CONFIG_PATH = os.path.join(ROOT_PATH,'config/config.yaml')
#print(ROOT_PATH)
#print(CONFIG_PATH)

class configReader():

    #读取配置文件内容
    def get_config_value(self,element):
        if os.path.exists(CONFIG_PATH):
            with open(CONFIG_PATH,'rb') as f :
                self.config_value = yaml.safe_load(f.read()).get(element)
            return self.config_value
        else:
            raise FileNotFoundError("配置文件不存在")

    #读取url内容
    def get_url(self):
        value = self.get_config_value("http")
        return value

    #读取其它配置的内容
    #读取log配置内容
    def get_log(self):
        value = self.get_config_value("logger")
        return value
    def get_database(self):
        value = self.get_config_value("database_info")
        return value
    #读取邮件配置
    def get_email(self):
        value = self.get_config_value("email_info")
        return value

    #读取获取token的必要信息
    def get_token_config(self):
        value = self.get_config_value("common_token")
        return value


if __name__ == '__main__':
    c = configReader()
    print(c.get_url()['timeout'])
    m = c.get_log()
    print(m)
    print(c.get_log()['console_level'])










