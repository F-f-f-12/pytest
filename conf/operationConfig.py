from conf.setting import FILE_PATH
import configparser
# configparser库，用于读取和解析配置文件（通常是 .ini 文件）

# 读取ini配置文件
class OperationConfig:
    def __init__(self,file_path=None):
        if file_path is None: # 默认路径为conf
            self.__file_path = FILE_PATH['conf']
        else:
            self.__file_path = file_path
        self.conf = configparser.ConfigParser() # 通过类ConfigParser，用来读取、解析和操作配置文件
        try:
            self.conf.read(self.__file_path,encoding='utf-8') # 读取配置文件
        except Exception as e:
            print(e)

    # session是ini头部值，option是选项的key值
    def get_section_for_data(self,section,option):
        try:
            data = self.conf.get(section, option) # 根据配置文件中的头部值和key值获取相应的value
            return data
        except Exception as e:
            print(e)

if __name__ == '__main__':
    oper = OperationConfig()
    print(oper.get_section_for_data('api_envi', 'host'))
