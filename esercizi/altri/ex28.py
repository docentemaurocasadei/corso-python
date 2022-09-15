#   Scrivi una funzione "v" che sia in grado di spedire delle eMail tramite un smtp! (aiuto: puoi usare il modulo smtplib)
import smtplib

def sendMail(subject, body):
    smtp_user = 'corso2@soluzionesoftware.com'
    smtp_password = '**********'

    sent_from = smtp_user
    to = ['docentemaurocasadei@gmail.com']

    email_text = """\
    From: %s
    To: %s
    Subject: %s
    
    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtps.aruba.it', 465)
        server.ehlo()
        server.login(smtp_user, smtp_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print('Email sent!')
    except Exception as ex:
        print('Something went wrong...' + ex.__str__())


sendMail(subject='Test', body='Ciao, \nCome va?')
