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

