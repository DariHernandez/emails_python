#! pyhton3

import imapclient, pyzmail, pprint, imaplib
from datetime import date

# Update the number of bytes to use in the program
imaplib._MAXLINE = 10000000

# Contect to imap server 
imapObj = imapclient.IMAPClient ("imap.gmail.com", ssl=True)

# Login to email account
imapObj.login ("darialternative@gmail.com", "AliciaParadoxa1999x3")

# Print list of email folders
# pprint.pprint(imapObj.list_folders())

# Use inbox folder
imapObj.select_folder ("INBOX", readonly=True)

# Seach emails (get uid: unique identifiers)
email_uids = imapObj.search (["ON", date(2021, 1, 26)])

# Control variables
max_emails = 100
total_emails = 0

# loop for each email identifier
for uid_index in range(len(email_uids)-1, 0, -1): 

    # Get the raw content of the last email
    rawMessages = imapObj.fetch([email_uids[uid_index]], ['BODY[]', 'FLAGS'])

    # Process email as pzmail object
    message = pyzmail.PyzMessage.factory(rawMessages[email_uids[uid_index]][b'BODY[]'])

    # Get email information
    subject = message.get_subject()
    from_email = message.get_addresses('from')[0]
    to_email = message.get_addresses('to')[0]
    body = message.text_part.get_payload().decode(message.text_part.charset)


    # print email information
    print ("\n")
    print(subject)
    print(from_email)
    print(to_email)
    # print(body)
    print ("\n")

    # Limit the number of emails
    total_emails += 1
    if total_emails == max_emails: 
        break

imapObj.logout()


