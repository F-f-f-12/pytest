# -*- coding:utf-8 -*-
import pytest
from common.recordlog import logs

# 测试用例前后置处理
@pytest.fixture(scope='session',autouse=True)
def fixture_test():
    logs.info("===========接口测试开始===========")
    yield
    logs.info("===========接口测试结束===========")
