#   Scrivi una funzione che data in ingresso una lista A contenente n parole, restituisca in output una lista B di interi che rappresentano la lunghezza delle parole contenute in A.
def lunghezze(l):
    return [len(v) for v in l]

def lunghezze2(l):
    l2 = []
    for v in l:
        l2.append(len(v))

print(lunghezze(['gatto', 'cane', 'cavallo', 'rinoceronte', 'topo']))
print(lunghezze2(['gatto', 'cane', 'cavallo', 'rinoceronte', 'topo']))
