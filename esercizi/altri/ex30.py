# Scrivi una funzione "file_backup" che sia in grado di effettuare copie di backup di determinati tipi di file, con le seguenti caratteristiche:
#
# Percorso da scansionare, di backup e tipologia di file da copiare dovranno essere passati dall'utente tramite input
# Il programma dovrà verificare la presenza o meno di una cartella di backup al percorso fornito, e qualora questa non fosse presente dovrà crearla
# La funzione dovrà anche gestire l'eventuale scelta da parte dell'utente, di un percorso da scansionare che non esiste
import os
import shutil

folder = input('inserisci il percorso da copiare (' + os.getcwd() + '\\immagini) :')
extension = input('inserisci il tipo di file (default: jpg):')
folder_backup = input('inserisci il percorso di backup' + os.getcwd() + '\\backup' + ':')
if folder == '':
    folder = os.getcwd() + '\\immagini'
if extension == '':
    extension = 'jpg'
if folder_backup == '':
    folder_backup = os.getcwd() + '\\backup'

if not os.path.exists(folder):
    print(f'path non esiste {folder}')
    exit(404)
if not os.path.exists(folder_backup):
    print('path non esiste (folder_backup)')
    exit(404)
# giving file extension
ext = (extension,)

# iterating over all files
for file in os.listdir(folder):
    if file.endswith(ext):
        shutil.copyfile(folder + '\\' + file, folder_backup + '\\' + file)
    else:
        continue
else:
    print('copia terminata')