import smtplib

conn = smtplib.SMTP('smtp-mail.outlook.com', 587)


conn.ehlo()
conn.starttls()
conn.login('mail@hotmail.com', 'Paassword')
conn.sendmail('from@hotmail.com', 'to@hotmail.com', 'Subject: Subject text\n\nMain body\n\n')
conn.quit()
