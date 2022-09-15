# Scrivi una funzione generatrice di password.
#
# La funzione deve generare una stringa alfanumerica di lunghezza variabile.
import string, random
def genera_password(lunghezza = 8):
    str = ''
    for i in range(lunghezza):
        str += random.choice(string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.punctuation)
    return str


print(genera_password(lunghezza=16))