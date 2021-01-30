#! python3

"""
Code for my youtube course: Python emails.
Youtube chanel (in spanish): https://www.youtube.com/channel/UCXWTlKzN_udf9LGqlDsuByg
"""

import smtplib, os

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# List of recipents
to_emails = {
    "darialternative@yahoo.com": "Juan",
    "darialternative@outlook.com": "Maria",
    "darialternative@aol.com": "Alberto",
    "darialternative@gmail.com": "Dari",
}

# Contect to smtp server and port
smtpObj = smtplib.SMTP ('smtp.gmail.com', 587)

# Send hello to smtp
smtpObj.ehlo()

# Active encriptation
smtpObj.starttls()

# Login
smtpObj.login ("your_email@gmail.com", "your_password")

# Loop for each email in list
for email, name in to_emails.items(): 

    # Create multipart email
    message = MIMEMultipart('alternative')
    message["From"] = "darialternative@gmail.com"
    message["To"] = email
    message["Subject"] = "Tu pedido está en camino ;)"

    # Text part of trhe email
    text_part = "Rastrea tu pedido!"

    # Get html part from template
    template_path = "email_template_delivery.html"
    template_file = open(template_path, "r")
    html_part = template_file.read()
    html_part = html_part.replace ("[name]", name)


    # Crate the Mime parts of the email
    part1 = MIMEText (text_part, "plain")
    part2 = MIMEText (html_part, "html")

    # Attatch parts to the email
    message.attach (part1)
    message.attach (part2)

    # Send full email
    smtpObj.sendmail('darialternative@gmail.com', 
                        email, 
                        message.as_string())

    # Confirmation message
    print ("Correo enviado a {}".format (name))

# Close connection
smtpObj.quit()
