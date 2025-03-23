# -*- coding:utf-8 -*-

import random
from common.rwyaml import ReadWriteYamlData  # 加上common便于后续其他文件引用当前的debugtalk.py
import json

class DebugTalk:

    def __init__(self):
        self.rw_yaml = ReadWriteYamlData()

    def get_extract_order_data(self,data,randoms):
        if randoms not in [0,-1,-2]:
            return data[randoms -1] # randoms -1将列表的索引改为从1开始

    # 获取extract.yaml的数据，node_name是yaml文件中的key值，randoms是随机读取yaml文件中列表的数据
    def get_extract_data(self,node_name,randoms=None):
        data = self.rw_yaml.get_extract_yaml(node_name)
        if randoms is not None:
            randoms = int(randoms)
            data_value ={
                randoms: self.get_extract_order_data(data,randoms),
                0: random.choice(data), # 随机返回列表的其中一个
                -1: ','.join(data), # data必须为字符串类型，此处用逗号分割（返回全部数据）
                -2: ','.join(data).split(',') # data必须为字符串类型，此处用逗号分割，并用逗号分割为列表（返回用列表全部数据）
            }
            data = data_value[randoms]
        return data

    # 实现MD5加密
    def md5_params(self,params):
        return  params
        print('实现MD5加密')

if __name__ == '__main__':
    debug = DebugTalk()
    print(debug.get_extract_data('product_id','-1')) # 读取列表的第一个value值