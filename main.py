# 执行该脚本，运行整个框架的代码
import pytest

if __name__ == '__main__':
    pytest.main()
    # 可指定测试结果显示方式，可指定运行某个测试用例
    # pytest.main(['-vs','./testcase/Login/test_login.py']) # 测试用例路径为根目录下的相对路径

