import smtplib as smtplib
from email.mime.multipart import MIMEMultipart
import unicodecsv as uni
reader = uni.reader(open("your excel file path here","rb"))
emails = []
for row in reader:
	emails.append(row)
msg = MIMEMultipart()
msg['Subject'] = "Ignore message"
s = smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login("your email id here","your password here")
for i in range(1,len(emails)):
	print(emails[i])
	s.sendmail('your email id here again',emails[i],"the message you want to send ")
s.quit()

