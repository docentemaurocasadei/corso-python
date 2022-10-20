# siamo una azienda che partecipa a fiere internazionali
# durante le ultime 2 fiere sono stati acquisiti dei contatti
# fiera1 = {'alfa', 'beta', 'gamma', 'google'}
# fiera2 = {'iota', 'revenge', 'gamma', 'sigma', 'google'}
# ritornati in ufficio occorre identificare quale contatto è duplicato tra le 2 fiere
# per farlo:
# realizzare un loop con ciclo for
# all'interno del loop inserire una if con operatore in
#

fiera1 = {'alfa', 'beta', 'gamma', 'google'}
fiera2 = {'iota', 'revenge', 'gamma', 'sigma', 'google'}
contatti_duplicati = set()

for contatto in fiera1:
    if contatto in fiera2:
        print(f'{contatto} è duplicato')
        contatti_duplicati.add(contatto)    # aggiunge un elemento al set

print(contatti_duplicati)
# la stessa cosa con metodo intersection
contatti_duplicati2 = fiera1.intersection(fiera2)
print('contatti_duplicati2:', contatti_duplicati2)
