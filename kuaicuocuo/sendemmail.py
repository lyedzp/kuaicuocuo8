import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
# 发送邮箱服务器
smtpserver = 'smtp.qq.com'
#发送邮箱用户/密码
user = '1126966246@qq.com'
# 这里用邮箱SMTP授权码
password = 'pciqqlpmfowuhaij'
#发送邮箱
sender = '1126966246@qq.com'

#接受邮箱
receiver = '2560547068@qq.com'
#发送邮件主题
subject = 'Python email test'

# 发送邮件附件
sendfile = open('D:\\梁月娥_软件测试工程师(3).pdf','rb').read()
att = MIMEText(sendfile,'base64','utf-8')
att["Content-Type"] = "application/octet-stream"
att["Conten-Disposition"] = 'attachment;filename="test"'
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = subject
msgRoot.attach(att)

# 编写HTML类型的邮件正文

msg = MIMEText('<html><h1>你好</h1></html>','html','utf-8')
msg['Subject'] = Header(subject,'utf-8')

#连接发送邮件

smpt = smtplib.SMTP()
smpt.connect(smtpserver)
smpt.login(user,password)
smpt.sendmail(sender,receiver,msg.as_string())
smpt.sendmail(sender,receiver,msgRoot.as_string())
smpt.quit()
