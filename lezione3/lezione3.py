# collection
#list
l = [10, 15, 8, 4]
print(l, type(l), id(l))

l1 = list((30, 35, 40, 10))
print(l1, type(l1))

l2 = ['cane', 'gatto', 10, 2.5]
print('la lista ha n.', len(l2), 'elementi')
print('l\'elemento di posizione 0 è:', l2[0])   # \ escaping

print(l2[-3::2]) #    elementi 1 e 2

fattoria = ['mucca', 'toro', 'gallina', 'tacchino', 'pecora']
if 'gallina' in fattoria:
    print('la gallina è nella fattoria')
else:
    print('la gallina NON è nella fattoria')
fattoria[3] = 'cavallo' # lista è modificabile
print(fattoria)

# sostituzione di più elementi
fattoria[2:4] = ['gallo', 'piccione', 'quaglia', 'papera']
fattoria.append('gallina')
print(fattoria, 'lunghezza:', len(fattoria))

# il ciclo FOR
print('***** gli animali della fattoria *****')
for animale in fattoria:
    print(animale)
else:
    print('***** lista animali terminata *****')

lista_numeri = []
for numero in range(1000):
    lista_numeri.append(numero)
# print(lista_numeri)

# oppure list comprehension
lista_numeri1 = [pippo for pippo in range(1000)]
# print(lista_numeri1)
#aaa
#ordinare le liste
classe = ['Giacomo', 'Ali', 'Alessandro', 'guido', 'federica', 'Andrea', 'Giovanni', 'Alessandro',
          'Simone', 'Tobia', 'Andrea']
classe.sort(key=str.lower)
print(classe)



# esercizi per casa:
# 3_list
# 3_list_append_insert_remove
# 3_list_elements
# 3_list_copy
# 3_list_sort
# 3_list_range
