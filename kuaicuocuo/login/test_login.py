import unittest
import requests
import json
class Login(unittest.TestCase):
    """快搓搓登录测试"""
    def setUp(self):
        print('登录测试开始')

    def interface(self,path,**accountNumber):
        url = 'http://52.82.54.135:8091/%s'% path
        data = accountNumber
        res = requests.get(url=url,json = data)
        res = json.loads(res.text)
        yield (res['message'])
    def test_loginSucess(self):
        """登陆成功"""
        login = Login()
        result = login.interface('sso/loginByPhoneNumber0',phoneNumber='13073831547',validCode = '960196')
        self.assertIn('成功',next(result),'账号验证码都正确,登录失败')

    def test_login_codeError(self):
        """验证码错误"""
        login = Login()
        result = login.interface('sso/loginByPhoneNumber0', phoneNumber='13073831547', validCode='960196')
        self.assertIn('失败', next(result), '验证码失败，登录成功')
    def tearDown(self):
        print('测试结束')

if __name__ == "__main__":
    unittest.main