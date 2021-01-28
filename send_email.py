#! python3

import smtplib

# List of recipents
to_emails = [
    "darialternative@yahoo.com",
    "darialternative@outlook.com",
    "darialternative@aol.com"
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
for email in to_emails: 

    # Enviar correo
    smtpObj.sendmail('darialternative@gmail.com', 
                        email, 
                        'Subject: Email example\n\nThis is an example email')

    # Confirmation message
    print ("Correo enviado a {}".format (email))

# Cerrar conexión
smtpObj.quit()
