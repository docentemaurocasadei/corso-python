#   Scrivi una semplice funzione che converta un dato numero di giorni, ore e minuti, passati dall'utente tramite funzione input, in secondi.
def converti_secondi(giorni = 0, ore = 0, minuti = 0):
    return giorni * 24 * 60 * 60 + \
            ore * 60 * 60 + \
            minuti * 60


print(converti_secondi(giorni=2, ore=3, minuti=45))