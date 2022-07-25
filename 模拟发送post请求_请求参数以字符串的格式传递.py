import requests

# 获取请求的URL
url = "http://127.0.0.1:9000/api/mgr/sq_mgr/"
# 获取请求头信息，content-Type，并且需要以字典的的存储Content-Type
header = {"Content-Type":"application/x-www-form-urlencoded"}

# 获取请求的参数，以字符串的格式传递
payload = """action=add_course&data={
  "name":"初中化学852656",
  "desc":"初中化学课程",
  "display_idx":"4"
}"""
#  模拟发送post请求，requests库调用post()方法，来执行post请求
res = requests.post(url, data=payload.encode('UTF8'), headers=header) # 因为请求参数中有中文，所以需要进行编码。即 payload.encode('UTF8')
# 如果 Content-Type 为 x-www-form-urlencoded这种数据格式，则使用data 形参 来接收请求参数
# 如果Content-Type 为 json这种数据格式，则使用  json  形参来接收请求参数。

# 获取响应的主体内容
print(f"响应主体内容为：{res.json()}")

# 获取请求头信息
print(f"请求头信息为：{res.request.headers}")