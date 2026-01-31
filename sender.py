import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = os.getenv("SMTP_HOST") # Host for Outlook/Hotmail
port = 587  # For STARTTLS
sender_email = os.getenv("SENDER_EMAIL")
password = os.getenv("SENDER_PASSWORD") # Use an App Password for security

def send_email_notification(body: str, subject: str, receiver_email: str):
    msg = MIMEMultipart()
    msg['From'] = f"Gold price tracker<{sender_email}>"
    msg['To'] = receiver_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)
        print("notification has been sent")
