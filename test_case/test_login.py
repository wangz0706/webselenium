#encoding=utf-8
from common.my_unit import StartTest
from businessView.loginView import LoginView

class Test_Login(StartTest):

    def testlogin(self):
        self.logger.info('start test login')
        login=LoginView(self.driver)
        login.login_action()
        self.assertTrue(login.check_login())

#pass
# if __name__ == '__main__':
#     unittest.main()