# -*- coding:utf-8 -*-
import pytest
from common.rwyaml import ReadWriteYamlData
from common.sendrequets import SendRequests
from common.recordlog import logs

rw_yaml = ReadWriteYamlData()
class TestLogin:

    @pytest.mark.parametrize('params',rw_yaml.get_testcase_yaml('./testcase/Login/login_data.yaml'))
    def test_login01(self,params):
        url = params['baseInfo']['url']
        new_url = 'http://127.0.0.1:8787' + url
        logs.info("获取到接口的地址：{}".format(new_url))

        method = params['baseInfo']['method']
        logs.info("获取到接口的地址：{}".format(method))
        headers = params['baseInfo']['headers']

        data = params['testcases'][0]['data']
        logs.info("获取到接口的地址：{}".format(data))

        send = SendRequests()
        res = send.run_main(url=new_url,data=data,headers=None,method=method)
        logs.info("获取到接口的地址：{}".format(res))

    @pytest.mark.parametrize('params',rw_yaml.get_testcase_yaml('./testcase/Login/login_data.yaml'))
    def test_login02(self,params):
        url = params['baseInfo']['url']
        new_url = 'http://127.0.0.1:8787' + url

        method = params['baseInfo']['method']
        headers = params['baseInfo']['headers']

        data = params['testcases'][1]['data']

        send = SendRequests()
        res = send.run_main(url=new_url,data=data,headers=None,method=method)
        print("接口实际返回值：",res)