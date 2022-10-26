import random
# creare un gioco:
# scrivere a video "sai che numero sto pensando (da 1 a 10)?"
# chiedere all'utente: "inserisci il numero ti dirò se hai vinto:"
# importare la random.randint e generare un numero casuale
# se l'utente ha inserito lo stesso numero generato scrivere
# - Hai Vinto! altrimenti scrivere - Hai Perso!#

n_uscito = random.randint(1,10)
print('sai che numero sto pensando (da 1 a 10)?')
n_inserito = input('inserisci il numero ti dirò se hai vinto:')
if int(n_inserito) == n_uscito:
    print('Hai Vinto!')
else:
    print('Hai Perso!', n_uscito)
