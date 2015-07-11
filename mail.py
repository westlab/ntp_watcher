import smtplib

def send(text):
    SERVER = "localhost"
    # Please configure correct email
    FROM = "foo@west.sd.keio.ac.jp"
    TO = ["baz@west.sd.keio.ac.jp"] # must be a list

    SUBJECT = "NTPD Remote Buffer Overflow Vulnerability"

    TEXT = text

    # Prepare actual message
    msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n%s"
       % (FROM, ", ".join(TO), SUBJECT, TEXT))

    # Send the mail

    server = smtplib.SMTP(SERVER)
    server.sendmail(FROM, TO, msg)
    server.quit()
