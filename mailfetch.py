import getpass
import imaplib
import email


def fetch_emails(username, password, sender=None, subject=None):
    # create an IMAP4_SSL instance and login
    server = 'imap.mail.yahoo.com'
    imap = imaplib.IMAP4_SSL(server)
    imap.login(username, password)

    # select the INBOX mailbox
    imap.select('INBOX')

    # search for messages that match the specified criteria
    criteria = []
    if sender:
        criteria.append('FROM "{}"'.format(sender))
    if subject:
        criteria.append('SUBJECT "{}"'.format(subject))
    search_criteria = ' '.join(criteria)
    typ, data = imap.search(None, search_criteria)

    # loop through the list of message IDs returned by the search
    messages = []
    for msg_id in data[0].split():
        # fetch the message by ID
        typ, msg_data = imap.fetch(msg_id, '(RFC822)')

        # convert the message data to an EmailMessage object
        msg = email.message_from_bytes(msg_data[0][1])

        # add the message to the list of messages
        messages.append(msg)

    # close the mailbox and logout
    imap.close()
    imap.logout()

    return messages

# prompt the user for their Gmail credentials
username = input('Enter your Gmail address: ')
password = getpass.getpass('Enter your Gmail password: ')

# fetch emails from the inbox
emails = fetch_emails(username, password)

# print the subjects of the fetched emails
for email in emails:
    print('Subject:', email['Subject'])
