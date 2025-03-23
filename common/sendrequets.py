# -*- coding:utf-8 -*-
# 加上coding，避免由于格式问题乱码

import requests

# 封装接口的请求
class SendRequests(object):
    # 初始化
    def __init__(self):
        pass

    # get方法请求接口
    def get(self,url,data,headers):
        if headers is None:
            res = requests.get(url=url,params=data)
        else:
            res = requests.get(url=url,params=data,headers=headers)
        return res.json()

    # post方法请求接口
    def post(self,url,data,headers):
        if headers is None:
            res = requests.post(url=url,data=data,verify=False) # verify=False去掉https的证书校验
        else:
            res = requests.post(url=url,data=data,headers=headers,verify=False)
        return res.json()

    # put方法请求接口
    def put(self):
        pass

    # delete方法请求接口
    def delete(self):
        pass

    # 主函数,传参method确定用哪种读取方法
    def run_main(self,url,data,headers,method):
        res = None
        if method.upper() == 'GET': # 将method的值先转为大写，再比较，避免了前期维护测试用例method大小不统一的问题
            res = self.get(url,data,headers)
        elif method.upper() == 'POST':
            res = self.post(url,data,headers)
        else:
            print("目前仅支持get/post，如需使用其他请求方法，请在接口请求函数添加。")
        return res

# 测试用例数据
url = 'http://127.0.0.1:8787/dar/user/login'
headers = None
data = {
    "user_name": "test01",
    "passwd": "admin123"
    }
method = 'post'

# 用于判断当前脚本是否作为主程序运行，它的作用主要体现在模块化编程和代码复用方面
if __name__ == '__main__':
    send = SendRequests() # 初始化/实例化这个类，实例化对象
    res = send.run_main(url=url,data=data,headers=headers,method=method) # 调用参数
    print(res)