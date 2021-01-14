# src/utils/SMTP.py
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
 

class SMTP():

    def __init__(self, remitente, destinatario, asunto, mensaje):
        self.remitente = remitente
        self.destinatario = destinatario
        self.asunto = asunto
        self.mensaje = mensaje    
    
    def send_message(self):       
        # create message object instance
        msg = MIMEMultipart()
        
        # setup the parameters of the message
        password = "----"
        msg['From'] = self.remitente
        msg['To'] = self.destinatario
        msg['Subject'] = self.asunto
        
        # add in the message body
        msg.attach(MIMEText(self.mensaje, 'plain'))
        
        #create server
        server = smtplib.SMTP('smtp.gmail.com: 587')
        
        server.starttls()
        
        # Login Credentials for sending the mail
        server.login(msg['From'], password)
        
        try:
            # send the message via the server.
            server.sendmail(msg['From'], msg['To'], msg.as_string())
            
            server.quit()
            
            print ("successfully sent email to %s:" % (msg['To']))
        except:
            print("El correo no fue enviado por algún motivo")

 

