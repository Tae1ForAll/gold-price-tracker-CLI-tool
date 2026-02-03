# external modules
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# internal modules
import gprice.data_manager as data_manager
import gprice.model as model

def send_email_notification(body: str, subject: str, receiver_email: str):
    credentials = data_manager.load_credential()
    config = data_manager.load_config()
    sender = credentials.sender_email
    
    msg = MIMEMultipart()
    msg['From'] = f"Gold price tracker<{sender.email}>"
    msg['To'] = receiver_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP(config.smtp.server, config.smtp.port) as server:
        server.starttls()
        server.login(sender.email, sender.password)
        server.send_message(msg)
        print(f"notification has been sent: {msg}")
        
        
def check_email_credential(credential: model.CredentialInfo):
    config = data_manager.load_config()
    smtp = config.smtp
    sender = credential.sender_email
    
    try:
        with smtplib.SMTP(smtp.server, smtp.port, timeout=10) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()

            server.login(sender.email, sender.password)

        return True  # success
    
    except smtplib.SMTPAuthenticationError:
        return False

    except smtplib.SMTPConnectError:
        raise RuntimeError("Failed to connect to SMTP server")

    except smtplib.SMTPException as e:
        raise RuntimeError(f"SMTP error: {e}")