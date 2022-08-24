# creare una lista di tuple con nomi e cognomi [("gianni", "rossi"),("marco", "bianchi"), ("silvia", "verdi"), ("carolina", "neri")]
# creare una funzione che accetta nomi e cognomi e li stampa in maiuscolo

l = [("gianni", "rossi"), ("marco", "bianchi"), ("silvia", "verdi"), ("carolina", "neri")]


def printToUpper(*args):
    for a in args:
        print(a.upper(), end=" ")
    print(f"\n****")


for t in l:
    printToUpper(*t)
