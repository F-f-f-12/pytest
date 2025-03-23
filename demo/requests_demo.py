import requests
from requests import utils

# ==========================================POST==========================================
url_post = 'http://127.0.0.1:8787/dar/user/login'
headers_post = {'Content-Type': 'application/x-www-formurlencoded;charset=UTF-8'}
data_post = {
    "user_name": "test01",
    "passwd": "admin123"
}

 # post方法，该接口不用传headers
res_post = requests.post(url=url_post,data=data_post)

# print(res_post) # 返回默认值，即状态码
# print(res_post.text) # 返回文本类型
# print(res_post.text.encode().decode("unicode_escape")) # 如果返回的文本是二进制，可以encode进行转译；但是如果返回正常，再用encode就会乱码
# print(res_post.json()) # 返回json类型
# print(res_post.content) # 返回二进制内容


# ==========================================GET==========================================
url_get = 'http://127.0.0.1:8787/coupApply/cms/goodsList'
headers_get = {'Content-Type': 'application/x-www-formurlencoded;charset=UTF-8'}
data_get = {
    "msgType": "getHandsetListOfCust",
    "page": 1,
    "size": 20
}

 # get方法,传参用params
res_get = requests.get(url=url_get,params=data_get,headers=headers_get)

# print(res_get)
# print(res_get.text)
# print(res_get.json())
# print(res_get.content)


# ==========================================SESSION==========================================
# session会话，可以保持登录的身份验证
session = requests.session() # 这里必须得分两步写，不能一步到位session = requests.session.request×
res_session = session.request(method='get',url=url_get,params=data_get,headers=headers_get)
print(res_session.json())


# ==========================================COOKIE==========================================
# 一般从登录接口获取cookies,因为有的接口需要传cookies或者token
from requests import utils
res_cookie = session.request(method='post',url=url_post,data=data_post)
cookie = requests.utils.dict_from_cookiejar(res_cookie.cookies)
print(cookie)


# ==========================================DELETE==========================================
# requests.delete()

# =====================PUT=====================
# requests.put()
