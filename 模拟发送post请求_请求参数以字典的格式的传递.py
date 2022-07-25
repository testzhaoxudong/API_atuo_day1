import requests
# 获取请求的URL
url = "http://127.0.0.1:9000/api/mgr/sq_mgr/"
#  获取请求头信息，  以字典格式传递
header = {"Content-Type":"application/x-www-form-urlencoded"}
# 获取请求参数，  以  字典  格式传递
payload = {"action":"add_course",
           "data":'{"name":"初中化学874534","desc":"初中化学课程","display_idx":"4"}'}
# 模拟发送post请求， requests库调用post()方法
res = requests.post(url, data=payload)
# 如果请求参数以字典的格式传递，不需要进行编码
# 请求参数如果以字典的格式传递，可以不用指定 Content-Type，默认会以form-urlencoded数据格式来提交参数。

# 获取响应的主体内容
print(f"相应的主体内容为：{res.json()}")
# 获取请求头信息
print(f"请求头信息为：{res.request.headers}")


