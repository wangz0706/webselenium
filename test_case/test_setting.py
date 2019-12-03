#encoding=utf-8
from businessView.AlertsettingView import SettingView
from common.my_unit import StartTest
from common.common_fun import Common

class TestSetting(StartTest):

    def test_setting(self):
        sett=SettingView(self.driver)
        sett.third_partlogin()
        self.assertTrue(sett.check_login())
        self.logger.info('start change setting')
        sett.alert_set()

# if __name__ == '__main__':
#     unittest.main()
