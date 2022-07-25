import unittest
from parameterized import parameterized
from BeautifulReport import BeautifulReport

# 有如下几天测试用例。  列表 套 列表， 列表 套 元组， 元组 套 列表 ，元组 套 元组
data = [("sup", "s1234567", True),("sup", "s1234", False), ("su", "s1234567", False)]
# 登录接口
def login(username, password):
    if username == "sup" and password == "s1234567":
        return True
    else:
        return False
# 编写测试用例
class Test_login(unittest.TestCase):
    # 定义方法
    @parameterized.expand(data)   # 使用装饰器传递测试用例数据
    def test_login(self, user, psw, expected):
        "登录"
        result = login(user, psw)  # 实际的结果
        # 断言
        self.assertEqual(result, expected)

bf = BeautifulReport(unittest.makeSuite(Test_login))
bf.report("登录接口的测试报告", filename="测试报告")