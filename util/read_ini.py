#from setting.setting import config_ini_dir
import configparser
import os

# 获取当前文件的上一层路径
cur_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
caps_path = os.path.join(os.path.join(cur_path,'config'),'LocalElement.ini')

class Read_Ini(object): # 初始化
    def __init__(self,node = None):
        if node:
            self.node = node
        else:
            self.node = 'RegisterElement'  # 配置文件中的某个节点
        self.cf = self.load_ini()

    def load_ini(self):  # 加载文件
        cf = configparser.ConfigParser()  # 使用 configparser模块读取配置文件信息
        # cf.read(config_ini_dir)  # 配置文件所在路径
        cf.read(caps_path)
        
        return cf

    def get_value(self,key): # 获取配置文件中key的value值
        data = self.cf.get(self.node,key)
        return data