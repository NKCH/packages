from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, ssl


def emailNotication(data):
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "sanzu.sandeep@gmail.com"
    password = "enter the password"
    dest = ['sanzu.sandeep@gmail.com']
    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)

        the_msg = MIMEMultipart('alternative')
        the_msg['Subject'] = data.get('subject')
        the_msg['From'] = sender_email

        html = """<!DOCTYPE html>
            <html>
                <body style:>
                    <h2>Write Us</h2>
                    <ul style="font-size: 1rem;font-family: cursive;">
                        <li style="display: -webkit-box;"><b>Name</b>    : {{name}}</li>
                        <li style="display: -webkit-box;"><b>Email</b>   : {{email}}</li>
                        <li style="display: -webkit-box;"><b>Message</b> : {{message}}</li>
                    </ul>
                </body>
            </html>
            """.replace('{{name}}', data.get('name')).replace('{{email}}', data.get('email')).replace('{{message}}',
                                                                                                      data.get(
                                                                                                          'message'))

        html_plan = MIMEText(html, 'html')
        the_msg.attach(html_plan)

        server.sendmail("sender_email_id", dest, the_msg.as_string())

    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()
