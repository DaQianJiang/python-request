import os
import yaml


ROOT_PATH = os.path.dirname(os.path.abspath('.'))
CONFIG_PATH = os.path.join(ROOT_PATH,'config\config.yaml')

class configReader():

    #读取配置文件内容
    def get_configv_value(self,element):
        if os.path.exists(CONFIG_PATH):
            with open(CONFIG_PATH) as f :
                self.config_value = yaml.safe_load(f.read()).get(element)
            return self.config_value
        else:
            raise FileNotFoundError("配置文件不存在")

    #读取url内容
    def get_url(self):
        value = self.get_configv_value("base_url")
        return value

    #读取其它配置的内容
    #读取log配置内容
    def get_log(self):
        value = self.get_configv_value("logger")
        return value


if __name__ == '__main__':
    c = configReader()
    print(c.get_url())
    m = c.get_log()
    print(m)
    print(c.get_log()['console_level'])










