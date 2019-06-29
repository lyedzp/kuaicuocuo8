import unittest
import time
from HTMLTestRunner import HTMLTestRunner
# 定义测试目录
test_dir = './login/'
discover = unittest.defaultTestLoader.discover(test_dir,'test*.py')
now = time.strftime('%Y-%m-%d %H_%M_%S')
reportPath = './'+ now + '_' + 'report.html'
if __name__ == '__main__':
    file = open(reportPath,'wb')
    runner = HTMLTestRunner(
        stream=file,
        title='快搓搓登录接口测试',
        description='用例执行情况:'
    )
    runner.run(discover)
    file.close()