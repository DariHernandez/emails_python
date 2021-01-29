#! python3

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

# Conectarse al servidor y puerto
smtpObj = smtplib.SMTP ('smtp.gmail.com', 587)

# Send hello to smtp
smtpObj.ehlo()

# Activar método de encriptación
smtpObj.starttls()

# Iniciar sesión
smtpObj.login('darialternative@gmail.com', 'AliciaParadoxa1999x3')

# Loop for each email in list
for email, name in to_emails.items(): 

    # Create multipart email
    message = MIMEMultipart('alternative')
    message["From"] = "darialternative@gmail.com"
    message["To"] = email
    message["Subject"] = "Email Example HTML"

    # Text part of trhe email
    text_part = "Hello, suscribe to my youtube chanel!"

    # Get html part from template
    template_path = "python emails 8 | Enviar correos HTML |/email_template_simple.html"
    template_file = open(template_path, "r")
    html_part = template_file.read()

    # Crate the Mime parts of the email
    part1 = MIMEText (text_part, "plain")
    part2 = MIMEText (html_part, "html")

    # Attatch parts to the email
    message.attach (part1)
    message.attach (part2)

    # Enviar correo
    smtpObj.sendmail('darialternative@gmail.com', 
                        email, 
                        message.as_string())

    # Confirmation message
    print ("Correo enviado a {}".format (name))

# Cerrar conexión
smtpObj.quit()
