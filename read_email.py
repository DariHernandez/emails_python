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

# loop for each email identifier
for uid in email_uids: 

    # Get the raw content of the last email
    rawMessages = imapObj.fetch([uid], ['BODY[]', 'FLAGS'])

    # Process email as pzmail object
    message = pyzmail.PyzMessage.factory(rawMessages[uid][b'BODY[]'])

    # get email information
    print ("\n")
    print(message.get_subject())
    print("{}: {}".format(message.get_addresses('from')[0][0], message.get_addresses('from')[0][1]))
    # print(message.get_addresses('to')[0])
    # print(message.text_part.get_payload().decode(message.text_part.charset))
    print ("\n")

imapObj.logout()


