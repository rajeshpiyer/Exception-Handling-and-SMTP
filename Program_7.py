#Sending mail to multiple reciepients
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, recipients, subject, body, EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD):
    
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = ', '.join(recipients)
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
    server.starttls() 
    server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    server.sendmail(sender_email, recipients, message.as_string())
    server.quit()

sender_email = input("Enter your email address: ")
recipients = input("Enter recipient email addresses separated by commas: ").split(',')
subject = input("Enter the subject of the email: ")
body = input("Enter the body of the email: ")

EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
EMAIL_HOST_USER = '630d5b2fd6a3dd'
EMAIL_HOST_PASSWORD = 'be30f10dd15b1d'
EMAIL_PORT = '2525'

send_email(sender_email, recipients, subject, body, EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)