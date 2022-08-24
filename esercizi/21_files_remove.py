# dato un file di nome readme.txt:
# aprire il file
# leggere tutto il contenuto del file e stamparlo a video
# tornare all'inizio del file con il puntatore
# leggere il file riga per riga e stampare a video ogni riga

print('**********')
f = open('readme.txt')
print(f.read())

print('**********')
f.seek(0)
for line in f.readlines():
    print(line, end="")

f.close()
