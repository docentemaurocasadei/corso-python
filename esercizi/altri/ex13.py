#   definire una lista di nomi
#   Scrivi una funzione a cui vengono passati come parametro un nome richiesto tramite input all'utente
#   restituire e stampare output se l'elemento passato sia presente o meno nella lista.
#   Qualora l'elemento sia presente nella lista, la funzione dovrà inoltre comunicarci l'indice dell'elemento.
soci = list(('gianni', 'silvia', 'marco', 'sara', 'luca'))
def esclusivo(nome):
    if nome in soci:
        return {'presente': True, 'posizione': soci.index(nome)}
    else:
        return {'presente': False}

inp_nome = ''
while inp_nome != 'stop':
    inp_nome = input('inserisci il nome (stop per uscire):')
    print(esclusivo(inp_nome))
