# -*- coding:utf-8 -*-
# 加上coding，避免由于格式问题乱码
import os
import yaml
from conf.setting import FILE_PATH


# 获取yaml数据，以及写入接口返回数据到特定的yaml文件
class ReadWriteYamlData:
# ================================指定读取的yaml文件================================
    def __init__(self,yaml_file=None):
        if yaml_file is not None:
            self.yaml_file = yaml_file # 如果文件路径不为空，则取yaml_file
        else:
            self.yaml_file = FILE_PATH['default_file'] # 如果文件路径为空，则默认的yaml文件，登录文件

# ================================获取yaml文件的数据================================
    def get_testcase_yaml(self,yaml_file):
        try:
            with open(yaml_file,'r',encoding='utf-8') as f: # 用with可以在文件打开处理完成后，自动关闭
                yaml_data = yaml.safe_load(f) # 安全读取
                return yaml_data
        except Exception as e:
            print(e)

# ================================写入接口返回数据到特定的extract.yaml文件================================
    def write_yaml_data(self,value): # value是写入dict格式
        file_path = FILE_PATH['extract']
        if not os.path.exists(file_path): # 先判断是否存在该文件
            pass
        else: # 如果不存在该文件，则会创建文件并写入
            try:
                file = open(file_path, mode='w', encoding='utf-8') # mode='a'是追加写入，mode='w'是清空写入
                if isinstance(value,dict):
                    write_data = yaml.dump(value,allow_unicode=True,sort_keys=False)
                    file.write(write_data)
                else:
                    print('写入[extract.yaml]的数据必须是字典类型。')
            except Exception as e:
                print(e)
            finally:
                file.close() # 前面用的open，后面就得加close

# ================================读取extract.yaml文件================================
    # node_name为读取yaml文件的key值
    def get_extract_yaml(self,node_name):
        if os.path.exists(FILE_PATH['extract']):
            pass
        else:
            print('extract.yaml不存在')
            file = open(FILE_PATH['extract'], mode='w')
            file.close()
            print('extract.yaml创建成功')

        with open(FILE_PATH['extract'], mode='r', encoding='utf-8') as rf:
            extract_data = yaml.safe_load(rf)
            return extract_data[node_name]


# ================================执行测试用例================================
if __name__ == "__main__":
    # 获取yaml文件的数据
    yaml_file = '../testcase/Login/login_data.yaml'
    rw_yaml = ReadWriteYamlData()
    res = rw_yaml.get_testcase_yaml(yaml_file=yaml_file)[0]

    url = res['baseInfo']['url']
    new_url = 'http://127.0.0.1:8787' + url
    method = res['baseInfo']['method']
    data = res['testcases'][0]['data']

    # 执行测试用例
    from common.sendrequets import SendRequests # 引用文件里的类
    send = SendRequests()
    res = send.run_main(method=method,url=new_url,data=data,headers=None)
    # print(res)

    # 写入接口返回数据到特定的yaml文件
    token = res.get('token') # 从字典格式中，根据key获取value
    write_data = {}
    write_data['Token'] = token # 向字典里赋值
    rw_yaml.write_yaml_data(write_data)


    # 读取extract.yaml
    res2 = rw_yaml.get_extract_yaml('Token') # 这里的参数，要与extract.yaml的key值一致，大小写敏感
    print(res2)
