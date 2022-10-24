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

classe = ['alessandro', 'ali', 'giacomo', 'sara', 'simone', 'giovanni', 'tobia', 'patrizia']

for persona in classe:
    if persona == 'sara' or persona == 'patrizia':
        print(f'{persona} è donna')
        continue
    else:
        print(f'{persona} è uomo')
    print(f'{persona} salta')

classifica = [
                {'nome': 'marco', 'punti': 100},
                {'nome': 'gianni', 'punti': 90},
                {'nome': 'silvia', 'punti': 85},
                {'nome': 'stefano', 'punti': 82},
                {'nome': 'martino', 'punti': 75},
                {'nome': 'davide', 'punti': 70},
                {'nome': 'daniela', 'punti': 69},
                ]

podio = set()
for atleta in classifica:
    if len(podio) <= 2:
        podio.add(atleta['nome'])
    else:
        break
print('hanno vinto:', list(podio))