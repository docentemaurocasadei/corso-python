#   creare una list classe composta dai nomi dei presenti di oggi alle 9:10  #list
#   aggiungere l'elemento patrizia che è arrivata alle 9:11 #append
#   stampare la lista dei presenti alle 9:15    #print
#   richiedere all'utente quale nome vuole verificare se presente #input
#   stampare nome è presente o NON è presente in base alla lista    #if
#definisco la classe
classe = ['Giacomo', 'Ali', 'Alessandro', 'Guido', 'Federica', 'Andrea', 'Giovanni', 'Alessandro',
          'Simone', 'Tobia', 'Andrea']
print('sono presenti alle 9:10:', len(classe), ' persone')

#entra patrizia
classe.append('patrizia')
print('sono presenti alle 9:15:', len(classe), ' persone')

# verifico un presente
nome = input('verifica un presente, inserisci il nome:')    # è case SENSITIVE
if nome in classe:
    print('è presente', nome)
    # oppure format
    print('è presente {}'.format(nome))
    # oppure f-string
    print(f'è presente {nome}')
else:
    print(nome, 'NON è presente')