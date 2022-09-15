#   Scrivi una funzione a cui passare una stringa come parametro, e che restituisca un dizionario rappresentante la "frequenza di comparsa" di ciscun carattere componente la stringa.
def frequenzimetro(str):
    l2 = dict()
    for c in str:
        l2.update({c: str.count(c)})
    return l2

print(frequenzimetro('gatto'))
