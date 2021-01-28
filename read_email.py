#! pyhton3

import imapclient, pyzmail

# Contect to imap server 
imapObj = imapclient.IMAPClient ("imap.gmail.com", ssl=True)

# Login to email account
imapObj.login ("darialternative@gmail.com", "AliciaParadoxa1999x3")

# Use inbox folder
imapObj.select_folder ("INBOX", readonly=True)

# Seach emails (get uid: unique identifiers)
email_uids = imapObj.search ('ALL')

# Control variables
max_emails = 10
total_emails = 0

# loop for each email identifier
for uid_index in range(len(email_uids)-1, 0, -1): 

    # Get the raw content of the last email
    rawMessages = imapObj.fetch([email_uids[uid_index]], ['BODY[]', 'FLAGS'])

    # Process email as pzmail object
    message = pyzmail.PyzMessage.factory(rawMessages[email_uids[uid_index]][b'BODY[]'])

    # get email information
    print ("\n")
    print(message.get_subject())
    print("{}: {}".format(message.get_addresses('from')[0][0], message.get_addresses('from')[0][1]))
    # print(message.get_addresses('to')[0])
    # print(message.text_part.get_payload().decode(message.text_part.charset))
    print ("\n")

    # Limit the number of emails
    total_emails += 1
    if total_emails == max_emails: 
        break

imapObj.logout()


