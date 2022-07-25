import requests

# 获取请求的URL
url = "http://127.0.0.1:9000/api/mgr/sq_mgr/"
# 获取请求头信息， 以  字典的格式  传递
header = {"Content-Type": "application/x-www-form-urlencoded"}
# 获取请求参数， 以  字典的格式 传递 请求参数
payload = {"action":"delete_course",
           "id": 5324}
# 模拟发送delete请求， requests库调用delete方法
res = requests.delete(url, data=payload, headers=header)
# 获取响应主体内容
print(f"响应主体内容为：{res.json()}")
