from pprint import pprint

import requests   # 导入requests库

#  获取请求的URL
url = "http://127.0.0.1:9000/api/mgr/sq_mgr/"
#  获取请求的URL参数，以字典的格式传递
params = {"action":"list_course", "pagenum": 1, "pagesize": 20}
# 模拟发送get请求，requests调用get()方法模拟发送请求
res = requests.get(url, params=params)
# 获取响应的主体内容
pprint(f"相应的主体内容为:{res.json()}")
# 获取状态码
pprint(f"状态码为:{res.status_code}")
