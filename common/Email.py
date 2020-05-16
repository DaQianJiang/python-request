from common.config_reader import configReader

from common.log import Log
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from  email.header import Header
import datetime
from common.config_reader import ROOT_PATH
import os

REPORT_FILE = os.path.join(ROOT_PATH,"testReport")



class Email():
    config_email = configReader().get_email()
    logger = Log().get_log()

    def __init__(self):
        self.smtp_host = self.config_email['stmp_host']
        self.smtp_port = self.config_email['stmp_port']
        self.smtp_password = self.config_email['stmp_password']
        self.smtp_user = self.config_email['mail_user']
        self.mail_sender = self.config_email["sender"]
        self.mail_receivers = self.config_email["receiver"]
        self.revicer = []
        if self.mail_receivers:
            self.revicer = str(self.mail_receivers).split("/")
        else:
            self.logger.info("---邮件接收者为空-----")
        print(self.mail_receivers)
        print(self.revicer)
        self.mail_title = self.config_email["title"]
        self.mail_content = self.config_email["content"]
        self.mail_test_user = self.config_email["testuser"]
        self.mail_on_off = self.config_email["on_off"]
        self.data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.mail_subject = self.mail_title +" "+self.data
        #设置总的邮件体对象
        self.msg_root = MIMEMultipart("mixed")
    def set_mail_header(self):
        self.msg_root["subject"] = Header(self.mail_subject,"utf-8")
        self.msg_root["From"] = self.mail_sender
        self.msg_root["To"] = ";".join(self.revicer)
    def set_mail_content(self):
        self.content = MIMEText(self.mail_content,"plain","utf-8")
        self.msg_root.attach(self.content)

    def set_mail_file(self):
        if os.path.exists(REPORT_FILE):
            self.report = os.path.join(REPORT_FILE,"report.html")
            self.file = open(self.report,"rb").read()
            self.att_file = MIMEText(self.file,"base64","utf-8")
            self.att_file["Content-Type"]= 'application/octet-stream'
            self.att_file["Content-Disposition"] = 'attachment; filename="mail.txt"'
            self.msg_root.attach(self.att_file)
        else:
            raise FileNotFoundError("testReport文件未找到")

    def send_email(self):
        self.set_mail_header()
        self.set_mail_content()
        self.set_mail_file()
        try:
            self.smtp_server = smtplib.SMTP_SSL(self.smtp_host,self.smtp_port)
        except smtplib.SMTPConnectError as e:
            self.logger.error("服务器链接失败:",e)
        else:
            try:
                self.smtp_server.login(self.smtp_user,self.smtp_password)
            except smtplib.SMTPAuthenticationError as e:
                self.logger.error("服务器登陆失败:",e)
            else:
                try:
                    self.smtp_server.sendmail(self.mail_sender,self.revicer,self.msg_root.as_string())
                    self.smtp_server.quit()
                    self.logger.info("----邮件发送成功----")
                    self.logger.info("发件人%s,收件人%s",self.mail_sender,self.revicer)
                except smtplib.SMTPException as e:
                     self.logger.error("---发送邮件失败---:",e)

if __name__ == '__main__':
    email = Email()
    email.send_email()


