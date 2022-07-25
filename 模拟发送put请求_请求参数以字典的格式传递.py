import requests
# 获取请求的URL
url = "http://127.0.0.1:9000/api/mgr/sq_mgr/"
# 获取请求头信息， 以  字典的格式  传递
header = {"Content-Type":"application/x-www-form-urlencoded"}
# 获取请求参数，以字典的格式传递
payload = {"action":"modify_course",
           "id": 5324,
           "newdata":"""{"name":"初中化学","desc":"初中化学课程","display_idx":"4"}"""}
# 模拟发送put请求
res = requests.put(url, data=payload)
# 如果请求参数以字典的格式传递，可以不需要进行编码
# 如果请求参数以字典格式传递，也可以不需要指定Content-Type，此时默认会以 form-urlencoded格式传递请求参数
# 获取响应的信息
print(f"响应的主体内容为：{res.json()}")
# 获取请求头信息
print(res.request.headers)
