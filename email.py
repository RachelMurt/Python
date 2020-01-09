import smtplib, email.mime.text

me = "joe@my.org.com"                # Put your own email here
fred = "fred@his.org.com"            # And fred's email address here
your_mail_server = "mail.my.org.com" # Ask your system administrator

# Create a text message containing the body of the email.
# You could read this from a file, of course.
msg = email.mime.text.MIMEText("""Hey Fred,

I'm having a party, please come at 8pm.
Bring a plate of snacks and your own drinks.

Joe""" )

msg["From"] = me               # Add headers to the message object
msg["To"] = fred
msg["Subject"] = "Party on Saturday 23rd"

# Create a connection to your mail server
svr = smtplib.SMTP(your_mail_server)
response = svr.sendmail(me, fred, msg.as_string()) # Send message
if response != {}:
    print("Sending failed for ", response)
else:
    print("Message sent.")

svr.quit()                                   # Close the connection
