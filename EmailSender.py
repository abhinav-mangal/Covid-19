import smtplib

to = input('Enter the Email of Recipient:\n')

content = input('Enter the content for email:\n')


def SendEmail(to, content):
    server = smtplib.SMTP('sntp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('abhinav18mangal@gmail.com', 'Superman18abhinav')
    server.sendmail('abhinav18mangal@gmail.com', to, content)
    server.close()


SendEmail(to, content)
