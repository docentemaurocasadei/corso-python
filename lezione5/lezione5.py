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

francesco = {'nome': 'Francesco', 'età': 32, 'peso': 80}
print(francesco.keys())
print(francesco.values())
print(len(francesco))

#dictionary annidati
classe = {
            'marco': {'età': 30, 'peso': 75},
            'sara': {'età': 29, 'peso': 51},
            'debora': {'età': 38, 'peso': 55},
}
print(classe['marco'])

x=10
if x>20:
    print('è maggiore')
elif x == 20:
    print('è uguale')
else:
    print('è minore')

print('è maggiore') if 10>20 else print('è minore')