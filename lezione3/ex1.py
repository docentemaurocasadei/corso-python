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
classe.append('Patrizia')
print('sono presenti alle 9:15:', len(classe), ' persone')

#alle 12:30 arriva Tina, si siede a fianco ad Andrea
classe.insert(6, 'Tina')
print('sono presenti alle 12:30:', len(classe), ' persone')
print(classe)

#alle 13:00 arrivano Giuseppina e Sara
classe.extend(['Giuseppina', 'Sara'])
print('sono presenti alle 13:00:', len(classe), ' persone')
print(classe)

#alle 13:15 esce Giacomo
classe.remove('Giacomo')
#oppure
del classe[0]
print('sono presenti alle 13:15:', len(classe), ' persone')
print(classe)

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

