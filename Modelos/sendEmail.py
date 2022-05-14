from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

class SendEmail():
    def __init__(self) -> None:

        # create message object instance
        self._msg = MIMEMultipart()
        # setup the parameters of the message
        self._password = "pass"
        self._msg['From'] = "email"

        # create server
        self._server = smtplib.SMTP('smtp.gmail.com: 587')

        self._server.starttls()

        # Login Credentials for sending the mail
        self._server.login(self._msg['From'], self._password)

    def sendEmail(self, toEmail="email", descricao="Subscription", message="Corpo da mensssagem da vazia!"):
        # message = message
        # add in the message body
        self._msg.attach(MIMEText(message, 'plain'))

        self._msg['To'] = toEmail
        self._msg['Subject'] = descricao

        # send the message via the server.
        self._server.sendmail(self._msg['From'],
                              self._msg['To'], self._msg.as_string())

        self._server.quit()
