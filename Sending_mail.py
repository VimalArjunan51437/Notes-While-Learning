import smtplib

import stdiomask

def mail():
    
    sender='Example_mail' # Sender mail
    receivers = 'Example_mail' # Receiver mail
    password = stdiomask.getpass() # It will hide password ny using " * " 
    message= """Hi. We can Send mail using python by using this program """ # Message need to send to receiver

    server =smtplib.SMTP('smtp.gmail.com',587) 

    server.starttls()

    server.login(sender,password) # Login to mail

    print("Login Success") 

    server.sendmail(sender,receivers,message) # Send mail

    print("EMail has sent to mail.")

mail() # Calling the function..