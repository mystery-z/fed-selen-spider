import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import timedelta
from datetime import date

today = date.today()
today_date = str(today)


sender_email = "********@GMAIL.COM"
receiver_email = "********@GMAIL.COM"
password = "********"

message = MIMEMultipart("alternative")
message["Subject"] = "Federal Reserve News-" + today_date
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
html=open("parsed.html")
# Turn these into plain/html MIMEText objects
part2 = MIMEText(html.read(), "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
    
print("mail sent successfully")
