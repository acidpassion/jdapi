import requests
import json
import sys
from json2html import *
import smtplib
from email import encoders 
from email.header import Header 
from email.mime.text import MIMEText 
from email.utils import parseaddr 
from email.utils import formataddr 


def format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, "utf-8").encode(), addr))

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))



url = 'http://p.3.cn/prices/mgets?skuIds=' + ",".join(sys.argv[1:]) + '&type=1'
print(url)
re = requests.get(url)
jd = json.loads(re.text)
print(jd)
html = json2html.convert(json = jd)
print(html)


from_email = "placebo_o@126.com"
from_email_pwd = "Alex1984"
to_email = "placebo_o@126.com"
smtp_server = "smtp.126.com"
 
msg = MIMEText(html, "html", "utf-8")
msg["From"] = format_addr("%s" %(from_email))
msg["To"] = format_addr("%s" %(to_email))
msg["Subject"] = Header("Price Lists from JD for skuIds" + ",".join(sys.argv[1:]), "utf-8").encode()
 
server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_email, from_email_pwd)
server.sendmail(from_email, [to_email], msg.as_string())
server.quit()