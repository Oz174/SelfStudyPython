"""
This python file is for the facade design pattern, hiding the complexity of sending an email
"""
import smtplib

class EmailFacade:
    def __inint__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password

    def send_email(self, to_email, subject, msg):
        if "@" not in self.user:
            from_email = f"{self.user}@{self.host}"
        else:
            from_email = self.user
        message = ("From {0}\r\n"
               "To {1}\r\n"
               "Subject: {2}\r\n\r\n{3}".format(
            from_email,
            to_email,
            subject,
            msg))

        smtp= smtplib.SMTP(self.host)
        smtp.login(self.user, self.password)
        smtp.sendmail(from_email, [to_email], message)