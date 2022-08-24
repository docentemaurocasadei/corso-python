# creare un file con nome 'dacancellare.txt':
# importare la libreria os
# richiedere all'utente: vuoi cancellare il file (y/n)
# se y cancellare il file
# se n non cancellarlo
from os import remove

with open('dacancellare.txt', 'w') as f:
    pass

if input('vuoi cancellare il file (y/n)') == 'y':
    remove('dacancellare.txt')
