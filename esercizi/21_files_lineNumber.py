# dato un file di nome readme.txt:
# scrivere una funzione che dato il nome del file restituisca il numero di linee
# fare un esercizio sia con ciclo for che con list comprehension

def file_line_number(fname):
    with open(fname) as f:
        l = [1 for l in f.readlines()]
    return sum(l)




def fileLineNumber(nomeFile):
    ln = 0
    with open(nomeFile) as f:
        for line in f.readlines():
            ln += 1
    return ln

print(fileLineNumber("readme.txt"))
print(file_line_number("readme.txt"))