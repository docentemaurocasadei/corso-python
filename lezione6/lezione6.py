# x = 5
# y = 10
# if x < y:
#     pass
# print('ciao')

# l = ['aaa', 'bbb', 'ccc', 'ddd']
# # for
# print("**** for ****")
# for elemento in l:
#     print(elemento)
# else:
#     print('lista terminata')
# # while
# print("**** while ****")
# i = 0
# while i < len(l):
#     print(l[i])
#     i += 1
# else:
#     print('lista terminata')

# classe = ['alessandro', 'ali', 'giacomo', 'sara', 'simone', 'giovanni', 'tobia', 'patrizia']
#
# for persona in classe:
#     if persona == 'sara' or persona == 'patrizia':
#         print(f'{persona} è donna')
#         continue
#     else:
#         print(f'{persona} è uomo')
#     print(f'{persona} salta')
#
# classifica = [
#                 {'nome': 'marco', 'punti': 100},
#                 {'nome': 'gianni', 'punti': 90},
#                 {'nome': 'silvia', 'punti': 85},
#                 {'nome': 'stefano', 'punti': 82},
#                 {'nome': 'martino', 'punti': 75},
#                 {'nome': 'davide', 'punti': 70},
#                 {'nome': 'daniela', 'punti': 69},
#                 ]
#
# podio = set()
# for atleta in classifica:
#     if len(podio) <= 2:
#         podio.add(atleta['nome'])
#     else:
#         break
# print('hanno vinto:', list(podio))

numeri = [0, 1, 2, 3, 4, 5]
# aggiungere ad ogni elemento della lista il numero 4
for numero in numeri:
    numeri[numero] += 4

print(numeri)

# definire e stampare una lista, una tupla, un set e un dictionary
# la stampa deve essere sia della variabile che del suo type

l = [1,2,3]
print('lista: ', l, type(l))
t = (1,2,3)
print('tupla: ', t, type(t))
s = {1,2,3}
print('set: ', s, type(s))
d = {'nome': 'Marco', 'cognome': 'Rossi'}
print('dict: ', d, type(d))

