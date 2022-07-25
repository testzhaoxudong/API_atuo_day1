import json

# 定义一个字典
dict1 = {"name": "jack", "age": 20}
print(type(dict1))
# json.dumps() 把 字典 转换成  字符串
str1 = json.dumps(dict1)
print(type(str1))

# 定义一个字符串
str2 = '{"name": "jack", "age": 20}'
print(f"str2的类型为：{type(str2)}")
# json.loads()  把字符串 转换为 字典
dict2 = json.loads(str2)
print(f"dict2的类型为：{type(dict2)}")
