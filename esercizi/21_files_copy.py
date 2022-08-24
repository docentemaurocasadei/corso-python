#costruire una funzione che accetta come parametri 2 nomi di file
#sovrascrivere il contenuto di uno dei file passato con quello dell'altro

def fileCopy(sorgente, destinazione):
    with open(sorgente) as s:
        with open(destinazione, mode="w") as d:
            d.write(s.read())


fileCopy(sorgente="readme.txt", destinazione="readme copy.txt")
