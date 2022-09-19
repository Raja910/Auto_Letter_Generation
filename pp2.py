import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('1d2worker@gmail.com', '1d2worker@gmail')
server.sendmail('1d2worker@gmail.com',
                'r1a5j9a6@gmail.com',
                'hello it is working')
