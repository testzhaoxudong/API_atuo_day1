import requests
# 获取请求的url
url = "http://127.0.0.1:9000/api/mgr/sq_mgr/"
# 获取请求头信息，以  字典的格式  传递
header = {"Content-Type": "application/x-www-form-urlencoded"}
# 获取请求的参数， 以  字符串的格式传递
payload = "action=delete_course&id=5324"
# 模拟发送delete请求，requests库调用delete方法
res = requests.delete(url, data=payload, headers=header) # 因为请求参数中不存在 中文 ，所以不需要进行编码
# 获取响应的主体内容
print(f"相应的主体内容为:{res.json()}")