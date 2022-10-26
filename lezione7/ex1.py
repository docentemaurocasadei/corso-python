# creare una funzione che accetta 2 parametri login e password
# (la password in chiaro anche se non si potrebbe)
# se login == 'giovanni' e password == '1234'
# la funzione deve ritornare Vero
# in caso contrario deve ritornare falso
# richiedere all'utente i dati login e password
# stampare il messaggio
# Benvenuto + login se utente e password sono corretti
# Login Errata se utente e password NON sono corretti#

def accesso(login, password):
    if login == 'giovanni' and password=='1234':
        return True
    else:
        return False

login = input('inserisci l\'utente:')
password = input('inserisci la password:')
if accesso(login,password):
    print(f'Benvenuto {login}')
else:
    print('Login Errata o non riconosciuta')

