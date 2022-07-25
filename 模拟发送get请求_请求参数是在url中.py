import requests   # 导入requests
from pprint import pprint  # 导入漂亮打印的包

# 获取请求的URL
url = "http://127.0.0.1:9000/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20"
#  模拟发送get请求，调用get()方法来模拟发送get请求
res = requests.get(url)
# ===================================================获取响应的内容=================================================
# 获取响应的头信息
print(f"响应的头信息为：{res.headers}")
# python 2.6版本之前  %        Python 2.6  format        Python 3.6  F-string
# 格式：  F"要输出的内容{对象}-要输出的内容{对象1}"

# 获取响应的主体内容，返回的是经过处理的Unicode型的数据
print(f"响应的主体内容为:{res.text}")

# 获取响应的主体内容，以json格式呈现
print(f"响应的主体内容以json格式呈现：{res.json()}")
pprint(f"响应的主体内容以json格式呈现：{res.json()}")   # pprint  ----  pretty print

# 获取响应的主体内容，以二进制的形式呈现
print(f"响应的结果以二进制形式呈现为：{res.content}")

# 获取响应的状态码
print(f"响应的状态码为：{res.status_code}")

# 获取响应的原因短语
print(f"响应的原因短语为：{res.reason}")

# 获取Cookies信息
print(f"获取Cookie信息：{res.cookies}")

# 获取响应的URL
print(f'响应的URL为：{res.url}')
# ===================================================获取请求的内容=================================================
# 获取请求头信息
print(f"请求头信息为：{res.request.headers}")

# 获取请求的URL
print(f"请求的URL为：{res.request.url}")

# 获取请求的主体信息
print(f"请求的主体内容为：{res.request.body}")



