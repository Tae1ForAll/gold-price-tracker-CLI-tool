# external modules
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# internal modules
import gprice.data_manager as data_manager
import gprice.model as model
import gprice.utils as utils

def send_email_notification(body: str, subject: str, receiver_email: str, show_log=True):
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
        
        if show_log:
            utils.print_auto(f"notification has been sent: {msg}")
        
        
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
        utils.print_error("Authentication failed, Please re-check your email and app password")
        return False

    except smtplib.SMTPConnectError:
        utils.print_error("Failed to connect to SMTP server")
        return False
    
    except Exception:
        utils.print_error("Unexpected Error, Please check your internet connection")
        return False