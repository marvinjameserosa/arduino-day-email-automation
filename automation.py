import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os  
import csv
from datetime import datetime


load_dotenv()

# SMTP configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587
your_email = os.getenv("EMAIL")
your_password = os.getenv("PASSWORD")

# CC email list
cc_email_list = []
  
subject = "Join Us for Arduino Day Philippines 2025!"

email_list = "partnership.csv"

log_file = "email_log.csv"

if not os.path.exists(log_file):
    with open(log_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp", "recipient", "cc", "status", "error_message"])

def log_email(recipient, cc_list, status, error_message=""):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, recipient, ", ".join(cc_list), status, error_message])

def duplicate_checker(log_file):
    emailed = []
    log = pd.read_csv(log_file)
    for index, row in log.iterrows():
        emailed.append(row["recipient"])
    return emailed

def send_email(recipient, recipient_email,):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = os.getenv("NAME")
    msg['To'] = recipient_email
    msg['Cc'] = ', '.join(cc_email_list)

    # HTML content for the email
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
        <div>test</div>
    </html>
    """

    msg.attach(MIMEText(html_content, 'html'))

    to_addresses = [recipient_email] + cc_email_list

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(your_email, your_password)
            server.sendmail(your_email, to_addresses, msg.as_string())
        
        print(f"Email sent successfully to {recipient} and CC'd to {', '.join(cc_email_list)}!")
        log_email(recipient, cc_email_list, "Success") 
        print("")
    
    except Exception as e:
        error_msg = str(e)
        print(f"Failed to send email to {recipient}: {error_msg}")
        log_email(recipient, cc_email_list, "Failed", error_msg)  

if __name__ == "__main__":
    email = pd.read_csv(email_list)
    emailed = duplicate_checker(log_file)

    for index, row in email.iterrows():
        recipient = row["recipient"]
        recipient_email = row['email']
        if recipient not in emailed:
            send_email(recipient, recipient_email)


