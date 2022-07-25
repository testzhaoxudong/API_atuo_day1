# 测试用例数据
data = [[{"username":"sup", "password":"s1234567"}, True],
        [{"username":"sup", "password":"s1234"}, False],
        [{"username": "su", "password": "s1234567"}, False]]


# 登录接口
def login(data):
    if data["username"] == "sup" and data["password"] == "s1234567":
        return True
    else:
        return False


# 使用parameterized 编写测试脚本