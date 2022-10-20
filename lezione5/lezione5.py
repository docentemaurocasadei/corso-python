#   set
s = {'marco', 'silvia', 'stefano', 'debora'}
print(type(s), s, len(s))

# s1 = set((1, 2, 3, 4))
# # equivale
# s1 = {1, 2, 3, 4}
#
# d = {'nome': 'Marco', 'cognome': 'Rossi'}
# d = dict(nome='Marco', cognome='Rossi')
# print(type(d), d)

# print(s[0]) # il set non è accessibile tramite indici
i = 0
for elemento in s:
    i += 1
print(i)

nome = 'marco'
if nome in s:
    print(f'{nome} sei iscritto!!')
else:
    print(f'{nome} non sei iscritto!!')

# print('stiamo cercando {}'.format(nome))
# print(f'stiamo cercando {nome}')