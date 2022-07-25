import requests

# 获取请求的URL
url = "http://127.0.0.1:9000/api/mgr/sq_mgr/"
# 获取请求头信息, 以  字典  的格式来传递
header = {"Content-Type": "application/x-www-form-urlencoded"}
# 获取请求参数， 以字符串的格式传递
payload = 'action=modify_course&id=5724&newdata={"name":"初中化学","desc":"初中化学课程","display_idx":"4"}'
#  模拟发送put请求，requests库调用put()方法模拟发送请求
res = requests.put(url, data=payload.encode("utf-8"), headers=header)
# 因为请求参数中有中文，所以需要进行编码。即 payload.encode('UTF8')

# 获取响应的结果
print(f"响应的结果为：{res.json()}")
# print(res.status_code)