import requests

#  获取请求的URL
url = "http://127.0.0.1:5000/file"
#  需要上传文件，则需要读取到文件的内容
# 方法一：传输格式： {"参数名":文件对象}    文件对象就是使用 open() 函数读取到的文件的内容就是文件对象
# 我们强烈建议你用二进制模式（binary mode）打开文件。这是因为 requests 可能会为你提供 header 中的 Content-Length，
# 在这种情况下该值会被设为文件的字节数。如果你用文本模式打开文件，就可能碰到错误。
# file = {"filename":open(r"C:\Users\Administrator\Desktop\file.txt", "rb")}

# 如果接口文档中规定了文件的类型，使用如下这种方式来上传的文件
# 方法二：传输格式： {"参数名":(文件名, 文件对象, 文件类型)}
file = {"filename":("file.txt", open(r"C:\Users\Administrator\Desktop\file.txt", "rb"), "text")}
# 模拟发送post请求，requests调用post方法
res = requests.post(url, files=file)

# 获取响应的主体内容
print(res.text)

# 获取请求头信息
print(res.request.headers)


