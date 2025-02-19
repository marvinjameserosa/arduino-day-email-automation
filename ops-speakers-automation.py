import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def read_html_template(file_path):
    """Read the HTML template from a file."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        print(f"Error reading HTML template: {e}")
        return None

def send_email(to_list, cc_list, subject, html_template, smtp_server, smtp_port):
    try:
        # Get sender credentials from environment variables
        sender_email = os.getenv("SENDER_EMAIL")
        sender_password = os.getenv("SENDER_PASSWORD")
        
        # Create message container
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = ", ".join(to_list)
        msg['Cc'] = ", ".join(cc_list)
        msg['Subject'] = subject
        
        # Attach HTML content
        msg.attach(MIMEText(html_template, 'html'))
        
        # Establish connection with SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure connection
        server.login(sender_email, sender_password)
        
        # Send email
        recipients = to_list + cc_list
        server.sendmail(sender_email, recipients, msg.as_string())
        server.quit()
        
        print(f"Email sent successfully to {', '.join(to_list)} and CC: {', '.join(cc_list)}")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Read the HTML template from file
html_template = read_html_template("email-template/speakers.html")

if html_template:  # Proceed only if the template was read successfully
    send_email(
        to_list=["recipient1@example.com", "recipient2@example.com"],
        cc_list=["cc1@example.com", "cc2@example.com"],
        subject="Test Email",
        html_template=html_template,
        smtp_server="smtp.gmail.com",
        smtp_port=587
    )
