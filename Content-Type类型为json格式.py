import  requests

# 获取请求的URL
url = "http://127.0.0.1:9000/apijson/mgr/sq_mgr/"
# 获取请求头信息
header = {"Content-Type": "application/json"}
# 获取请求参数
json_data = {
  "action" : "add_course_json",
  "data"	 : {
    "name":"初中化学123654",
    "desc":"初中化学课程",
    "display_idx":"4"
  }
}
# 模拟发送post请求，如果不指定Content-Type，则默认以 application/json格式来传递请求参数。
res = requests.post(url, json=json_data)
# 获取响应的主体内容
print(f"响应的主体内容为:{res.json()}")
# 获取请求头信息
print(f'请求头信息为：{res.request.headers}')
