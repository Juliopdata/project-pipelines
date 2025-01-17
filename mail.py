import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
import re
load_dotenv()


# Check if email is right written

def checkMail(email):
    while True:
        regex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if(re.search(regex,email)):  
            return email.lower()  
        else:  
            email=input('Please input a valid email:')

# Send email

def sendMail (email,report):
    subject = "Your RottenTomatoes recommendation"
    body = "Your info is in the attached PDF"
    sender_email = "pipelinesjulio@gmail.com"
    receiver_email = email
    password = os.getenv("PASWORD_GMAIL")

# Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

# Add body to email
    message.attach(MIMEText(body, "plain"))

    filename = report[1]  # In same directory as script
    filepath = report[0]

    # Open PDF file in binary mode
    with open(filepath, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)

sendMail('juliopdata@gmail.com', ['./output/recommendation.pdf', 'recommendation.pdf' ])