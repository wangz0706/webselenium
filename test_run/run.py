#encoding=utf-8
from HTMLTestRunner import HTMLTestRunner
import time,os
from common.Email import SendMail
import unittest

now = time.strftime("%Y-%m-%d %H_%M_%S")
report_name = now + 'testfanreport.html'
report_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),"reports",report_name)

def getsuit():
    suit=unittest.TestSuite()
    case_path=os.path.join(os.path.dirname(os.path.dirname(__file__)),'test_case')
    suit=unittest.defaultTestLoader.discover(case_path,'test*.py')

    with open(report_path,'wb') as f:
        runner = HTMLTestRunner(stream=f,title='web selenium',description=u"testfan 的Ui自动化测试")
        runner.run(suit)

if __name__ == '__main__':
    getsuit()
    m = SendMail(
        username='18215615874@163.com', passwd='123456Aa', recv='zhenzhen.wang@dianrong.com,18215615874@163.com',
        title=u'web的Ui自动化测试', content=report_path, file=report_path)
    m.send_mail()
