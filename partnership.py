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
                <tr style="vertical-align: top;">
                <td style="word-break: break-word; border-collapse: collapse !important; vertical-align: top;">
                    
                    <!-- Main Content Wrapper -->
                    <div style="padding: 0; background-color: transparent; width: 100%; max-width: 650px; margin: 0 auto; word-wrap: break-word; background-color: #ffffff;">
                    
                    <!-- Header Image -->
                    <table role="presentation" cellpadding="0" cellspacing="0" width="100%" style="font-family: 'Source Sans Pro', sans-serif;">
                        <tr>
                        <td align="center" style="padding: 0;">
                            <img src="header.png" alt="Header" style="display: inline-block; width: 100%; max-width: 650px; border: none; height: auto;">
                        </td>
                        </tr>
                    </table>

                    <!-- Content Section -->
                    <table role="presentation" style="font-family: 'IBM Plex Sans', sans-serif; width: 100%; border: 0;" cellpadding="0" cellspacing="0">
                        <tr>
                        <td style="padding: 24px; text-align: center; word-break: break-word;">
                            <h2 style="margin: 0; font-size: 16px; font-weight: 400; color: #000000; line-height: 140%;">
                            <strong>Empowering Makers, Igniting Innovation!</strong>
                            </h2>
                        </td>
                        </tr>
                    </table>

                    <!-- Email Body -->
                    <table role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                        <tbody>
                        <tr>
                            <td style="word-break: break-word; padding: 24px 40px; color: #000000; font-family: 'IBM Plex Sans', sans-serif;" align="left">
                            
                            <p style="font-size: 14px; line-height: 160%; text-align: justify;">
                                <strong>Dear {recipient},</strong>
                            </p>
                            <p style="font-size: 14px; line-height: 160%; text-align: justify;">
                                We are excited to announce that preparations are underway for <strong>Arduino Day Philippines 2025</strong>, a celebration of creativity, collaboration, and innovation in the tech community, happening on <strong>March 22.</strong>
                            </p>
                            <p style="font-size: 14px; line-height: 160%; text-align: justify;">
                                We are reaching out to invite your organization to partner with us in bringing this year’s event to life. Arduino Day Philippines continues to empower students, professionals, and hobbyists to explore, innovate, and showcase groundbreaking projects—and your support has always been instrumental in making it all possible.
                            </p>
                            <p style="font-size: 14px; line-height: 160%; text-align: justify;">
                                Attached, you’ll find our sponsor kit, which outlines this year’s event objectives, sponsorship packages, and the benefits of being part of this incredible journey. Together, we can create a platform for meaningful workshops, inspiring talks, and the sharing of ideas that shape the future.
                            </p>
                            <p style="font-size: 14px; line-height: 160%; text-align: justify;">
                                We would be honored to have your organization join us in fostering a culture of innovation and collaboration. If you have any questions or would like to discuss further, please don’t hesitate to reach out.
                            </p>

                            <!-- Links -->
                            <div style="font-size: 14px; line-height: 100%; text-align: center; margin-top: 20px;">
                                <p>
                                <strong>Arduino Day 2025 Primer:</strong> 
                                <a href="#" style="text-decoration: none; color: #003333; font-weight: bold;" target="_blank">Click Here</a>
                                </p>
                                <p>
                                <strong>Last Year's Event Highlights:</strong> 
                                <a href="#" style="text-decoration: none; color: #003333; font-weight: bold;" target="_blank">Click Here</a>
                                </p>
                            </div>

                            <!-- Signature -->
                            <p style="font-size: 14px; line-height: 160%; text-align: justify; margin-top: 20px;">
                                Best Regards,
                            </p>
                            <p style="font-size: 14px; line-height: 160%; text-align: justify;">
                                <strong>Arduino Day Philippines Team</strong>
                            </p>

                            <!-- Logo -->
                            <div style="text-align: center; padding-top: 32px; padding-bottom: 32px;">
                                <img src="logo.png" style="width: 117.24px; height: 56.7px;" />
                            </div>

                            </td>
                        </tr>
                        </tbody>
                    </table>

                    <!-- Footer with Social Media Links -->
                    <table role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0" style="background-color: #C9C6C6; padding: 32px 0;">
                        <tbody>
                        <tr>
                            <td style="text-align: center;">
                            
                            <!-- Social Icons -->
                            <div style="text-align: center; margin: 20px 0;">
                                <a href="#" style="display: inline-block; width: 32px; height: 32px; padding: 0 10px; text-align: center;">
                                <img src="tiktok.png" alt="TikTok" style="width: 24px; height: 24px; vertical-align: middle;"/>
                                </a>
                                <a href="#" style="display: inline-block; width: 32px; height: 32px; padding: 0 10px; text-align: center;">
                                <img src="facebook.png" alt="Facebook" style="width: 32px; height: 32px; vertical-align: middle;"/>
                                </a>
                                <a href="#" style="display: inline-block; width: 32px; height: 32px; padding: 0 10px; text-align: center;">
                                <img src="linkedin.png" alt="LinkedIn" style="width: 30px; height: 30px; vertical-align: middle;"/>
                                </a>
                                <a href="#" style="display: inline-block; width: 32px; height: 32px; padding: 0 10px; text-align: center;">
                                <img src="gmail.png" alt="Gmail" style="width: 26px; height: 24px; vertical-align: middle;"/>
                                </a>
                            </div>  

                            <!-- Copyright -->
                            <div style="font-size: 14px; font-weight: 400; line-height: 18px; text-align: center; color: #000000; font-family: 'Source Sans Pro', sans-serif;">
                                Copyright © 2025 Arduino Day Philippines
                            </div>

                            </td>
                        </tr>
                        </tbody>
                    </table>

                    </div>
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
