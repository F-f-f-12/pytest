
import os
from common.rwyaml import ReadWriteYamlData
from common.debugtalk import DebugTalk
import json


class BaseRequests:

    def __init__(self):
        self.rw_yaml = ReadWriteYamlData()

    # 从yaml文件提取并解析有${}格式的数据，并进行替换
    def replace_load(self, data):
        str_data = data
        if not isinstance(data, str):  # 如果data不是字符串类型，则将其转换为字符串
            str_data = json.dumps(data, ensure_ascii=False) # ensure_ascii=False正常读取中文

        for i in range(str_data.count('${')):
            if "${" in str_data and "}" in str_data:
                # index检测是否是字符串，并找到字符串的索引位置
                start_index = str_data.index('$') # 查找字符 $ 首次出现的位置（索引）
                end_index = str_data.index('}', start_index) # 从 start_index 位置开始查找字符 } 首次出现的位置
                ref_all_params = str_data[start_index:end_index + 1] # 按索引取出该变量字符串
                print(ref_all_params)

                # 取出函数名
                func_name = ref_all_params[2:ref_all_params.index('(')] # 索引从2开始，到左括号结束
                print(func_name)
                # 取出函数里面的参数值
                func_params = ref_all_params[ref_all_params.index('(')+1: ref_all_params.index(')')] # 索引从左括号+1开始，到右括号结束
                print(func_params)
                # 传入替换的参数，获取对应的值
                print("yaml文件替换解析前：",str_data)
                # 反射机制
                extract_data = getattr(DebugTalk(),func_name)(*func_params.split(',') if func_params else "")
                """
                getattr(DebugTalk(), func_name)：动态获取 DebugTalk() 实例中名为 func_name 的属性/方法
                (*func_params.split(',') if func_params else "")：
                如果 func_params 不为空字符串，则将其按逗号 , 分割成列表，并通过 * 解包为函数参数。
                如果 func_params 为空字符串，则传递一个空字符串 "" 作为参数。
                """

                str_data = str_data.replace(ref_all_params, str(extract_data)) # 替换测试用例里的值
                print("yaml文件替换解析后：", str_data)


        # 还原数据
        if data and isinstance(data, dict): # 检查data是否不为空，以及是否是字典类型
            data = json.loads(str_data) # 如果 data 是字典类型，则将 str_data（字符串形式的 JSON 数据）解析为 Python 字典
        else:
            data = str_data # 如果 data 不为空或不是字典类型，则将 str_data 赋值给 data，保持数据的字符串形式
        return data


if __name__ == '__main__':
    rw_yaml = ReadWriteYamlData()
    data = rw_yaml.get_testcase_yaml('../testcase/Login/login_data.yaml')[0] # 文件路径为：../testcase/Login/login_data.yaml，不是：./testcase/Login/login_data.yaml
    print(data) # 先读取测试用例中的数据
    base = BaseRequests()
    res = base.replace_load(data) # 再替换测试用例中的变量数据
    print(res)

