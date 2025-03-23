# 1. python常用的数据类型有：str,list,int.float,dict,set,tuple

# 2. json序列化和反序列化
# json序列化，其实就是将python中的字典转换为字符串
import json
res = {'token':'6e75Bac7bE048A5BCE3F4D5Ec5FBD'}
json_str = json.dumps(res, ensure_ascii=False) # 双引号为字符串
print(json_str)
print(type(json_str))
# 输出：
# {"token": "6e75Bac7bE048A5BCE3F4D5Ec5FBD"}
# <class 'str'>


# json反序列化，其实就是将python中的字符串转换为字典
import json
res = "token"
json_dict = json.loads(json_str) # 单引号为字典
print(json_dict)
print(type(json_dict))
# 输出：
# {'token': '6e75Bac7bE048A5BCE3F4D5Ec5FBD'}
# <class 'dict'>
