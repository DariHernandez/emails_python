#! python3

import smtplib

# List of recipents
to_emails = {
    "darialternative@yahoo.com": "Juan",
    "darialternative@outlook.com": "Maria",
    "darialternative@aol.com": "Alberto"
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

    # Enviar correo
    smtpObj.sendmail('darialternative@gmail.com', 
                        email, 
                        'Subject: Email example\n\nGood morning {} This is an example email'.format(name))

    # Confirmation message
    print ("Correo enviado a {}".format (name))

# Cerrar conexión
smtpObj.quit()
