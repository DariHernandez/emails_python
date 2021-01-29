#! pyhton3

import imapclient, pyzmail, pprint, imaplib

# Update the number of bytes to use in the program
imaplib._MAXLINE = 10000000

# Contect to imap server 
imapObj = imapclient.IMAPClient ("imap.gmail.com", ssl=True)

# Login to email account
imapObj.login ("darialternative@gmail.com", "AliciaParadoxa1999x3")

pprint.pprint(imapObj.list_folders())

# Use inbox folder
imapObj.select_folder ("INBOX", readonly=False)

# Seach emails (get uid: unique identifiers)
email_uids = imapObj.search ('ALL')

# Get the last email in folder
last_email = email_uids.pop()

# Get the raw content of the last email
rawMessages = imapObj.fetch([last_email], ['BODY[]', 'FLAGS'])

# Process email as pzmail object
message = pyzmail.PyzMessage.factory(rawMessages[last_email][b'BODY[]'])

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

# Seen and unseen
# imapObj.add_flags ([last_email], "\Seen")
# imapObj.remove_flags ([last_email], "\Seen")

# Answered and unanwered
# imapObj.add_flags ([last_email], "\Answered")
# imapObj.remove_flags ([last_email], "\Answered")

# Flagged and unflagged
# imapObj.add_flags ([last_email], "\Flagged")
# imapObj.remove_flags ([last_email], "\Flagged")

# Draft and undraft
# imapObj.add_flags ([last_email], "\Draft")
# imapObj.remove_flags ([last_email], "\Draft")

# Recient and unrecient
# imapObj.add_flags ([last_email], "\Recent")
# imapObj.remove_flags ([last_email], "\Recent")

# Deleted and undeleted
# imapObj.add_flags ([last_email], "\Deleted")
# imapObj.remove_flags ([last_email], "\Deleted")

# print ("Flag updated")


# Move email to specific folder
imapObj.move ([last_email], "[Gmail]/Papelera")

print ("Email moved")

imapObj.logout()


