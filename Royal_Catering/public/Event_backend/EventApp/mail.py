import smtplib
import getpass

def sendmail(mail,data):
    print(mail,data,"hjhgkhkjhkhkhkgljg")

    HOST = "smtp-mail.outlook.com"
    PORT = "587"

    FROM_EMAIL = "rahulrajeshh4@outlook.com"
    TO_EMAIL = mail
    PASSWORD = "Poiuytrewq@12#"

    SUBJECT = "Test Mail"
    BODY = data

    message = f"Subject:{SUBJECT}\n\n{BODY}"
 
    smtp = smtplib.SMTP(HOST, PORT)

    status_code,responce = smtp.ehlo()
    print(f"[*] Echoing the server: {status_code}{responce}")

    status_code,responce = smtp.starttls()
    print(f"[*] Starting TLS connection: {status_code}{responce}")

    status_code,responce = smtp.login(FROM_EMAIL,PASSWORD)
    print(f"[*] Starting TLS connection: {status_code}{responce}")

    smtp.sendmail(FROM_EMAIL,TO_EMAIL,message)
    smtp.quit() 