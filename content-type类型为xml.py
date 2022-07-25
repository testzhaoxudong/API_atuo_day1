import requests

# 获取请求的URL
url = "http://127.0.0.1:5000/xml"
#  获取请求的参数
body = """<?xml version="1.0"?>
<a>
   <username value="vampire"/>
</a>"""
#  模拟发送post请求
res = requests.post(url, data=body)
# 获取响应的结果
print(f"响应的结果为：{res.text}")