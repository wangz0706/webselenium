# encoding: utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

#将测试报告通过邮件发送，邮件内容和附件都是html格式的
class SendMail(object):
    def __init__ (self, username, passwd, recv, title, content,
              file=None,email_host='smtp.163.com', port=25):
        self.username = username
        self.passwd = passwd
        self.recv = recv
        self.title = title
        self.content = content
        self.file = file
        self.email_host = email_host
        self.port = port


    def send_mail (self):
        msg = MIMEMultipart()
        f = open(self.content, 'rb')
        mail_body = f.read()
        f.close()
        msg_html1 = MIMEText(mail_body, 'html', 'utf-8')
        msg.attach(msg_html1)
        # msg.attach(MIMEText(mail_body))  # 邮件正文的内容
        # 发送内容的对象
        if self.file:  # 处理附件的
            # att = MIMEText(open(self.file).read())
            att = MIMEApplication(open(self.file, 'rb').read())
            # att["Content-Type"] = 'application/octet-stream'
            att["Content-Disposition"] = 'attachment; filename="%s"' % self.file
            msg.attach(att)
        # msg.attach(MIMEText(self.content))#邮件正文的内容
        msg['Subject'] = self.title  # 邮件主题
        msg['From'] = self.username  # 发送者账号
        msg['To'] = self.recv  # 接收者账号列表
        self.smtp = smtplib.SMTP(self.email_host, port=self.port)
        # 发送邮件服务器的对象
        self.smtp.login(self.username, self.passwd)
        try:
            self.smtp.sendmail(self.username, self.recv, msg.as_string())
        except Exception as e:
            print('出错了。。', e)
        else:
            print('发送成功！')

    def __del__ (self):
        self.smtp.quit()
