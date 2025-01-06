import smtplib

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    try:
        server.login('clnarayanan12345@gmail.com','GMAILQWERTYUIOP')
        server.sendmail('clnarayanan12345@gmail.com',to,content)
        server.close()
    except Exception as e:
        print(e)
        print("some error in function block")
mailid= "clnarayanan234@gmail.com"
try:
    print("Content of the mail sir?")
    content = input()
    to = mailid
    sendEmail(to,content)
    print("Sent succesfuly!")
except Exception as e:
    print(e)
    print("Some error occured in sending the mail sir!")