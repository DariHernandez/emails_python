#! python3

import smtplib, os
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate

# List of recipents
to_emails = {
    "darialternative@yahoo.com": "Juan",
    "darialternative@outlook.com": "Maria",
    "darialternative@aol.com": "Alberto"
}

file_list = [
    "python emails 6 | Adjuntar archivos a correos | email.mime/file.pdf",
    "python emails 6 | Adjuntar archivos a correos | email.mime/img.jpg"
]

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

    # Make an instance of mime multipart to create the message
    message = MIMEMultipart()

    # Add main part to the email
    message['From'] = "darialternative@gmail.com"
    message["To"] = email
    message["Date"] = formatdate(localtime=True)
    message["Subject"] = "Email with file"

    # Add tex5t to the email
    text = 'Good morning {} This is an example email'.format(name)
    message.attach (MIMEText(text))

    # Loop for files in list
    for file in file_list:

        # Read file and create email part 
        file_binary = open(file, "rb")
        part = MIMEApplication(file_binary.read(), name=os.path.basename(file))
        file_binary.close()

        # Add file to the message
        part['Content-Disposition'] = 'attachment; filename="{}"'.format(os.path.basename(file))
        message.attach(part)

    # Enviar correo
    smtpObj.sendmail('darialternative@gmail.com', 
                        email, 
                        message.as_string())

    # Confirmation message
    print ("Correo enviado a {}".format (name))

# Cerrar conexión
smtpObj.quit()
