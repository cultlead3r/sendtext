import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_text(email, pas, smtp, port, sms_gateway, msg_subject, msg_content):
    '''Use this to send the text.
    
    Args:
    -----
        email: your email address that you're sending from (str)
        pas: the password for your email (str)
        smtp: the smtp server address you're sending from
        port: the port the smtp server you're sending from runs on
        sms_gateway: the phone number @ provider gateway you're sending to
                     for example for Verizon, 1112223333@vzwpix.com
        msg_subject: subject of text (str)
        msg_content: content of text (str)
    
    List of cell providers gateway email addresses:
    
    AT&T: number@txt.att.net (SMS), number@mms.att.net (MMS)
    T-Mobile: number@tmomail.net (SMS & MMS)
    Verizon: number@vtext.com (SMS), number@vzwpix.com (MMS)
    Sprint: number@messaging.sprintpcs.com (SMS), number@pm.sprint.com (MMS)
    Xfinity Mobile: number@vtext.com (SMS), number@mypixmessages.com (MMS)
    Virgin Mobile: number@vmobl.com (SMS), number@vmpix.com (MMS)
    Tracfone: number@mmst5.tracfone.com (MMS)
    Simple Mobile: number@smtext.com (SMS)
    Mint Mobile: number@mailmymobile.net (SMS)
    Red Pocket: number@vtext.com (SMS)
    Metro PCS: number@mymetropcs.com (SMS & MMS)
    Boost Mobile: number@sms.myboostmobile.com (SMS), number@myboostmobile.com (MMS)
    Cricket: number@sms.cricketwireless.net (SMS), number@mms.cricketwireless.net (MMS)
    Republic Wireless: number@text.republicwireless.com (SMS)
    Google Fi (Project Fi): number@msg.fi.google.com (SMS & MMS)
    U.S. Cellular: number@email.uscc.net (SMS), number@mms.uscc.net (MMS)
    Ting: number@message.ting.com
    Consumer Cellular: number@mailmymobile.net
    C-Spire: number@cspire1.com
    Page Plus: number@vtext.com'''
    server = smtplib.SMTP(smtp,port)
    server.starttls()
    server.login(email,pas)
    
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = sms_gateway
    msg['Subject'] = f'{msg_subject}'
    body = f'{msg_content}'
    # can also send html content.
    msg.attach(MIMEText(body, 'plain'))
    sms = msg.as_string()

    server.sendmail(email,sms_gateway,sms)
    server.quit()


# send_text(email, pas, smtp, port, sms_gateway, "Hi subject", "Hi message.")