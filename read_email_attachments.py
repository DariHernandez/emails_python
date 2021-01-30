#! pyhton3

"""
Code for my youtube course: Python emails.
Youtube chanel (in spanish): https://www.youtube.com/channel/UCXWTlKzN_udf9LGqlDsuByg
"""

import imapclient, pyzmail, imaplib, os

# Update the number of bytes to use in the program
imaplib._MAXLINE = 10000000

# Folder to save attatchment files
folder_download = "files"

# Contect to imap server 
imapObj = imapclient.IMAPClient ("imap.gmail.com", ssl=True)

# Login to email account
imapObj.login ("your_email@gmail.com", "your_password")

# Use inbox folder
imapObj.select_folder ("INBOX", readonly=True)

# Seach emails (get uid: unique identifiers)
email_uids = imapObj.search ('ALL')

# Control variables
max_emails = 6
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

    print ("Files: ")


    # Loop for each part in the email
    for index_part in range (1, len(message.get_payload())): 
        
        # Read each file in the current part
        for part in message.get_payload(index_part).walk():

            file_name = part.get_filename()
            print ("- {}".format(file_name))

            # Verify the name of the file
            if file_name: 

                # Create path of file
                file_path = os.path.join (folder_download, file_name)
                
                # Save file
                file_obj = open (file_path, "wb")
                file_obj.write (part.get_payload(decode=True))
                file_obj.close()

           
    # Limit the number of emails
    total_emails += 1
    if total_emails == max_emails: 
        break

imapObj.logout()


