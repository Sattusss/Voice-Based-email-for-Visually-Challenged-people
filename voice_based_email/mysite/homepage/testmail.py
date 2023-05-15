import smtplib

def send_email(subject, body, sender, receiver):
    # SMTP settings for Yahoo Mail
    smtp_server = 'mail.digipodium.com'
    smtp_port = 587

    # Email account credentials
    email_username = 'satyamtiwari4430@digipodium.com'
    email_password = 'projectforblind'

    # Compose the email headers and body
    email_message = f"From: {sender}\nTo: {receiver}\nSubject: {subject}\n\n{body}"

    try:
        # Open a secure SMTP connection
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(email_username, email_password)

            # Send the email
            server.sendmail(sender, receiver, email_message, )

        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error message: {str(e)}")

# Usage example
send_email("Hello from Python", "This is the body of the email.", "satyamtiwari4430@digipodium.com", "satyamsln2001@gmail.com")
