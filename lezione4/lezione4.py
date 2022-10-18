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