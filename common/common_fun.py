#encoding=utf-8
import logging
import time,os
from baseView.BaseView import BaseView

class Common(BaseView):
    def setlog(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(level=logging.INFO)
        # 1）使用下面的后执行会有警告，不影响结果。。不使用下面的clear，其他地方调用时会生成重复的日志
        # self.logger.handlers.clear()
        #判断logger是否已经添加过handler，是则直接返回logger对象，否则执行handler设定以及addHandler(ch)
        if not self.logger.handlers:
            # 控制台输出
            consle=logging.StreamHandler()
            self.logger.addHandler(consle)
            t = time.strftime('%Y_%m_%d')
            logname = "Apptestlog" + t + ".log"
            #logname = "Apptestlog" + ".log"
            logpath = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs",logname)
            #  使用encoding = 'utf-8'解决生成的log中文乱码问题
            filehandler = logging.FileHandler(logpath,encoding='utf-8')
            formatter = logging.Formatter('%(asctime)s - %(filename)s -[line:%(lineno)d] - %(levelname)s - %(message)s')
            filehandler.setFormatter(formatter)
            self.logger.addHandler(filehandler)
        return self.logger

    def gettime(self):
        self.now=time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    def getScreenshot(self,module):
        time=self.gettime()
        file=os.path.dirname(os.path.dirname(__file__)) + '/screenshots/%s_%s.png'%(module,time)
        self.logger.info('get screenshot %s'%module)
        self.driver.get_screenshot_as_file(file)


# if __name__ == '__main__':
#     cc=Common()
#     cc.setlog().info('common ok?')
