#   In Svezia, i bambini giocano spesso utilizzando un linguaggio un po' particolare detto "rövarspråket", che significa "linguaggio dei furfanti": consiste nel raddoppiare ogni consonante di una parola e inserire una "o" nel mezzo. Ad esempio la parola "mangiare" diventa "momanongogiarore".
#
# Scrivi una funzione in grado di tradurre una parola o frase passata tramite input in "rövarspråket".
#
# Dopo aver tradotto una frase, il programma dovrà chiedere all'utente se intende tradurne un'altra, e in caso di risposta positiva, dovrà attendere l'inserimento di una nuova parola da parte dell'utente.
vocali = "aeiou"
def traduci(parola):
    parola_out = ''
    for c in parola:
        if c not in vocali:
            parola_out += c + 'o' + c
        else:
            parola_out += c
    return parola_out

inp_parola = ''
while inp_parola != 'stop':
    inp_parola = input('inserisci la parola (stop per uscire):')
    print(traduci(inp_parola))
