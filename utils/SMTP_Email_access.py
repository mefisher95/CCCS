import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from mysite import app


class SMTP_EmailAccess:
    def __init__(self):

        self.email = app.config['DNR_EMAIL']
        self.pas = app.config['DNR_PW']
        self.smtp = 'smtp.gmail.com'
        self.port = 587
        self.smtp_server = None
        # self.imap_server = None
        # self.gateways = ['mms.att.net', 'myboostmobile.com', 'pm.spirit.com',
        #                  'email.uscc.net', 'vtext.com', 'vmobl.com']
        # self.messages = []
        # self.now = timestamp


    def start(self):
        self.smtp_server = smtplib.SMTP(self.smtp, self.port)
        # self.smtp = smtplib.SMTP_SSL()
        # self.smtp.connect(self.smtp, self.port)
        self.smtp_server.starttls()
        self.smtp_server.login(self.email, self.pas)


    def stop(self):
        try: self.smtp_server.quit()
        except: pass


    def send_message(self, target, subject, message):
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'html'))
        sms = msg.as_string()

        self.smtp_server.sendmail(self.email, target, sms)

def send_email(target, subject, message):
    mail = SMTP_EmailAccess()
    mail.start()
    mail.send_message(target, subject, str(message))
    mail.stop()
