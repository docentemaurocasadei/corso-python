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

# nome = input('inserisci il nome:')
nome = 'marco'
if nome in s:
    print(f'{nome} sei iscritto!!')
else:
    print(f'{nome} non sei iscritto!!')

# print('stiamo cercando {}'.format(nome))
# print(f'stiamo cercando {nome}')

s.add('maria')
s.update({'carla', 'francesco'})

s.discard('giacomo')
valore_eliminato = s.pop()
# s.clear()
print(s)
print(valore_eliminato)

gara2 = {'lea', 'simona'}
s1 = s.union(gara2)
print(s)    # {'stefano', 'carla', 'francesco', 'debora', 'silvia', 'maria'}
print(s1)   #{'lea', 'simona', 'stefano', 'carla', 'francesco', 'debora', 'silvia', 'maria'}

s.update(gara2)
print(s)   #{'lea', 'simona', 'stefano', 'carla', 'francesco', 'debora', 'silvia', 'maria'}
