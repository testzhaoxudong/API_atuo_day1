import requests

# 获取请求的URL
url = "http://127.0.0.1:9000/api/mgr/sq_mgr/"
# 获取请求的URL参数，请求URL参数以 字符串的格式传递
params = "action=list_course&pagenum=1&pagesize=20"

# 模拟get请求，调用get()方法模拟发送get请求
res = requests.get(url, params=params)

# 获取响应的主体内容
print(f"响应的主题内容为：{res.json()}")
