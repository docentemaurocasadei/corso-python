# # intero
# i = 105
# # stringa
# s = 'ciao'
# # decimale
# d = 10.5
# print( type(i), i  )
# print(s.upper())
# print("oggi", 'è', 'il 18')

mia_frase = 'oggi è martedì 18 ottobre'
if 'Martedì'.upper() in mia_frase.upper():
    print('il giorno è martedì')
else:
    print('il giorno NON è martedì')

print(mia_frase.replace('martedì', 'mercoledì'))
età = 32
peso = '80Kg'
altezza = '180cm'
#metodo 1
print('Marco ha {} anni'.format(età))
#metodo 2
print(f'Marco ha {età} anni pesa {peso} ed è alto {altezza}')

# boolean
print(10>12) #False

risultato = 10 % 6
print(risultato)

x = 5
y = 10
y += x
# y = y + x
print('y è', y)

if x == y:
    print('sono ==')
else:
    print('sono !=')

colore_testo = 'rosso'
colore_sfondo = 'bianco'
if colore_testo == 'rosso' and colore_sfondo == 'rosso':
    print('il testo non è leggibile')
elif colore_testo == 'rosa' and colore_sfondo == 'rosso':
    print('il testo è poco leggibile')
else:
    print('il testo è leggibile')

carlo_eta = 40
carlo_peso = 75
carlo_altezza = 175
maria_eta = 32
maria_peso = 48
maria_altezza = 162
carlo = [40, 75, 175]
maria = [32, 48, 162]
simona = [25, 54, 168]
print(carlo, type(carlo))

colleghi = [carlo, maria, simona]

amici = [[45, 80, 185], [35, 60, 170], [21, 95, 198]]
amici.pop(0)

gianmaria = [25, 76, 178]
colleghi.append(gianmaria)  # aggiunge un elemento alla fine della lista

nuovi_colleghi = [[26, 90, 180], [28, 50, 160]]
colleghi.extend(nuovi_colleghi)
colleghi.append([26, 90, 180])
print(colleghi)

print(colleghi[2])

# dictionary
# chiave : valore
colleghi2 = {'carlo': [40, 75, 175],
             'maria': [32, 48, 162],
             'simona': [25, 54, 168]}
colleghi2['gianmaria'] = [25, 76, 178]
# print(colleghi2['Simona'])    # se non trovato è bloccante
# print(colleghi2.get('Simona'))  # se non trovato non è bloccante
colleghi2['simona'] = [25, 54, 168]
print(colleghi2)
print('fine')

#tuple
t_iscritti = ('Carlo', 'Francesco', 'Sabrina', 'Stefania')
print(t_iscritti, type(t_iscritti))

l_iscritti = ['Carlo', 'Francesco', 'Sabrina', 'Stefania']
print(l_iscritti, type(l_iscritti))

# t_iscritti[0] = 'Marco'
l_iscritti[0] = 'Marco'
print(t_iscritti)
print(l_iscritti)

colleghi3 = colleghi2.copy()
del colleghi2['carlo']
print(colleghi3)

print(len(colleghi3))

#esercizi per casa:
# 4_tuple, 4_tuple_elements, 4_tuple_modificare_come_list
# 6_dict, 6_dict_items, 6_dictionary, 6_dictionary_elements, 6_dictionary_elements_get