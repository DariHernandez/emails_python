#! python3

"""
Code for my youtube course: Python emails.
Youtube chanel (in spanish): https://www.youtube.com/channel/UCXWTlKzN_udf9LGqlDsuByg
"""

import smtplib

# List of recipents
to_emails = {
    "darialternative@yahoo.com": "Juan",
    "darialternative@outlook.com": "Maria",
    "darialternative@aol.com": "Alberto"
}

# Connect to server and port
smtpObj = smtplib.SMTP ('smtp.gmail.com', 587)

# Send hello to smtp
smtpObj.ehlo()

# Active encriptation
smtpObj.starttls()

# login
smtpObj.login ("your_email@gmail.com", "your_password")

# Loop for each email in list
for email, name in to_emails.items(): 

    # Send email
    smtpObj.sendmail('darialternative@gmail.com', 
                        email, 
                        'Subject: Email example\n\nGood morning {} This is an example email'.format(name))

    # Confirmation message
    print ("Correo enviado a {}".format (name))

# Close connection
smtpObj.quit()
