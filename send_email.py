#! python3

import smtplib

# Conectarse al servidor y puerto
smtpObj = smtplib.SMTP ('smtp.gmail.com.mx', 587)

# Send hello to smtp
smtpObj.ehlo()

# Activar método de encriptación
smtpObj.starttls()

# Iniciar sesión
smtpObj.login('darialternative@gmail.com', 'AliciaParadoxa1999x3')

# Enviar correo
smtpObj.sendmail('darialternative@gmail.com', 
                    'darialternative@yahoo.com', 
                    'Subject: Email example\n\nThis is an example email')

# Confirmation message
print ("Correo enviado")

# Cerrar conexión
smtpObj.quit()
