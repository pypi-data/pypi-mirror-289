import time
from smtplib import SMTP
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(
    event_type: str,
    file_path: str,
    smtp_server: str,
    smtp_port: int,
    smtp_user: str,
    smtp_password: str,
    sender_email: str,
    receiver_email: str,
):
    """
    Send an email notification about a file system event.

    Args:
        event_type (str): The type of the file system event.
        file_path (str): The path to the file that triggered the event.
        smtp_server (str): The SMTP server address.
        smtp_port (int): The SMTP server port.
        smtp_user (str): The SMTP server username.
        smtp_password (str): The SMTP server password.
        sender_email (str): The sender's email address.
        receiver_email (str): The receiver's email address.

    Returns:
        None
    """
    subject = f"File System Event: {event_type}"
    time_stamp = time.strftime("%Y-%m-%d %H:%M:%S")
    body = f"Event Type: {event_type}\nFile Path:\
 {file_path}\nTimestamp: {time_stamp}"

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            send_mail(
                server,
                msg,
                smtp_user,
                smtp_password,
                sender_email,
                receiver_email,
            )

    except Exception as e:
        print(f"Failed to send email: {e}")


def send_mail(
    server: SMTP,
    msg: MIMEMultipart,
    smtp_user: str,
    smtp_password: str,
    sender_email: str,
    receiver_email: str,
):
    """
    Send the email using the provided SMTP server and message.

    Args:
        server (SMTP): The SMTP server object.
        msg (MIMEMultipart): The email message to be sent.
        smtp_user (str): The SMTP server username.
        smtp_password (str): The SMTP server password.
        sender_email (str): The sender's email address.
        receiver_email (str): The receiver's email address.

    Returns:
        None
    """
    server.starttls()
    server.login(smtp_user, smtp_password)
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
