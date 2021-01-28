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

# Print all email uid
# print (email_uids)

# Get the las uid 
last_email_uid = email_uids.pop()

# Get the raw content of the last email
rawMessages = imapObj.fetch([last_email_uid], ['BODY[]', 'FLAGS'])

# Process email as pzmail object
message = pyzmail.PyzMessage.factory(rawMessages[last_email_uid][b'BODY[]'])

# get email information
print(message.get_subject())
print(message.get_addresses('from'))
print(message.get_addresses('to'))
print(message.text_part.get_payload().decode(message.text_part.charset))

imapObj.logout()


