import smtplib
from blowfish import create_encrypted
from email.mime.text import MIMEText

def send_mail(send_to_gmail,subject,message):
    gmail="prathyuma.v2020@vitstudent.ac.in"
    password="kqxualkkivycoohc"
    send_text = create_encrypted(message)

    # storing  the information to the server
    msg=MIMEText(send_text)
    msg['from']=gmail
    msg['to']=send_to_gmail
    msg['subject']=subject

    # To connect the server
    server= smtplib.SMTP_SSL('smtp.gmail.com',465)
    #To login to the server
    server.login(gmail,password)
    # Sending the mail
    server.sendmail(gmail,send_to_gmail,(msg.as_string()))
    print('Mail sent')
    # Exiting the server
    server.quit()