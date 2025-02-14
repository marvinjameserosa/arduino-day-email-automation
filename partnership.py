import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os  

load_dotenv()

# SMTP configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587
your_email = os.getenv("EMAIL")
your_password = os.getenv("PASSWORD")

# CC email list
cc_email_list = [""]
  
subject = "Join Us for Arduino Day Philippines 2025!"

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
        <table style="border-collapse: collapse; table-layout: fixed; border-spacing: 0; vertical-align: top; min-width: 320px; margin: 0 auto; background-color: #003333; width: 100%;" cellpadding="0" cellspacing="0">
            <tbody>
                <tr>
                <td style="word-break: break-word; border-collapse: collapse !important; vertical-align: top; padding: 0;">
                    
                    <!-- Main Content Wrapper -->
                    <table style="width: 100%; max-width: 650px; margin: 0 auto; background-color: #ffffff;" cellpadding="0" cellspacing="0">
                    
                    <!-- Header Image -->
                    <tr>
                        <td align="center" style="padding: 0;">
                        <img src="https://github.com/marvinjameserosa/arduino-day-email-automation/blob/master/email-template/header.png?raw=true" alt="Header" style="display: block; width: 100%; max-width: 650px; height: auto; border: none;">
                        </td>
                    </tr>

                    <!-- Content Section -->
                    <tr>
                        <td style="padding: 24px; text-align: center; font-family: 'IBM Plex Sans', sans-serif;">
                        <h2 style="margin: 0; font-size: 16px; font-weight: 400; color: #000000; line-height: 140%;">
                            <strong>Empowering Makers, Igniting Innovation!</strong>
                        </h2>
                        </td>
                    </tr>

                    <!-- Email Body -->
                    <tr>
                        <td style="padding: 24px 40px; color: #000000; font-family: 'IBM Plex Sans', sans-serif; text-align: left; word-break: break-word;">
                        
                        <p style="font-size: 14px; line-height: 160%;">
                            <strong>Dear {recipient},</strong>
                        </p>
                        <p style="font-size: 14px; line-height: 160%;">
                            We are excited to announce that preparations are underway for <strong>Arduino Day Philippines 2025</strong>, happening on <strong>March 22.</strong>
                        </p>
                        <p style="font-size: 14px; line-height: 160%;">
                            We invite your organization to partner with us in bringing this year’s event to life. Your support helps empower students, professionals, and hobbyists to innovate and showcase groundbreaking projects.
                        </p>
                        <p style="font-size: 14px; line-height: 160%;">
                            Attached, you’ll find our sponsor kit outlining event objectives, sponsorship packages, and benefits. Together, we can create meaningful workshops, inspiring talks, and a platform for idea-sharing.
                        </p>
                        <p style="font-size: 14px; line-height: 160%;">
                            We would be honored to have your organization join us. If you have any questions, please don’t hesitate to reach out.
                        </p>

                        <!-- Links -->
                        <div style="font-size: 14px; text-align: center; margin-top: 20px;">
                            <p>
                            <strong>Arduino Day 2025 Primer:</strong> 
                            <a href="#" style="text-decoration: none; color: #003333; font-weight: bold;">Click Here</a>
                            </p>
                            <p>
                            <strong>Last Year's Event Highlights:</strong> 
                            <a href="#" style="text-decoration: none; color: #003333; font-weight: bold;">Click Here</a>
                            </p>
                        </div>

                        <!-- Signature -->
                        <p style="font-size: 14px; line-height: 160%; margin-top: 20px;">
                            Best Regards,
                        </p>
                        <p style="font-size: 14px; line-height: 160%;">
                            <strong>Arduino Day Philippines Team</strong>
                        </p>

                        <!-- Logo -->
                        <div style="text-align: center; padding-top: 24px;">
                            <img src="https://github.com/marvinjameserosa/arduino-day-email-automation/blob/master/email-template/logo.png?raw=true" style="width: 117px; height: auto;">
                        </div>

                        </td>
                    </tr>

                    <!-- Footer -->
                    <tr>
                        <td style="background-color: #C9C6C6; text-align: center; padding: 24px;">
                        
                        <!-- Social Icons -->
                        <div style="margin: 10px 0; text-align: center;">
                            <a href="#" style="display: inline-block; margin: 0 10px; vertical-align: middle;">
                            <img src="https://github.com/marvinjameserosa/arduino-day-email-automation/blob/master/email-template/tiktok.png?raw=true" alt="TikTok" style="width: 24px; height: 24px;">
                            </a>
                            <a href="#" style="display: inline-block; margin: 0 10px; vertical-align: middle;">
                            <img src="https://github.com/marvinjameserosa/arduino-day-email-automation/blob/master/email-template/facebook.png?raw=true" alt="Facebook" style="width: 30px; height: 30px;">
                            </a>
                            <a href="#" style="display: inline-block; margin: 0 10px; vertical-align: middle;">
                            <img src="https://github.com/marvinjameserosa/arduino-day-email-automation/blob/master/email-template/linkedin.png?raw=true" alt="LinkedIn" style="width: 30px; height: 30px;">
                            </a>
                            <a href="#" style="display: inline-block; margin: 0 10px; vertical-align: middle;">
                            <img src="https://github.com/marvinjameserosa/arduino-day-email-automation/blob/master/email-template/gmail.png?raw=true" alt="Gmail" style="width: 26px; height: 24px;">
                            </a>
                        </div>              

                        <!-- Copyright -->
                        <p style="font-size: 14px; color: #000000; font-family: 'Source Sans Pro', sans-serif; margin: 0;">
                            Copyright © 2025 Arduino Day Philippines
                        </p>

                        </td>
                    </tr>

                    </table>
                </td>
                </tr>
            </tbody>
            </table>
    </html>
    """

    msg.attach(MIMEText(html_content, 'html'))

    # Combine recipient and CC addresses
    to_addresses = [recipient_email] + cc_email_list

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(your_email, your_password)
            server.sendmail(your_email, to_addresses, msg.as_string())
        print(f"Email sent successfully to {recipient} and CC'd to {', '.join(cc_email_list)}!")
    except Exception as e:
        print(f"Failed to send email to {recipient}: {e}")

if __name__ == "__main__":
  # Load the CSV file
  df = pd.read_csv('partnership.csv')
  print(df)

  # Iterate through the dataframe and send emails
  for index, row in df.iterrows():
    send_email(row['company_name'], row['email'])
