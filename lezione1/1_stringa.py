# print('oggi è il 29 settembre')
# voglio verificare se un numero è maggiore di un altro
# if 15 > 10:
#     print('è maggiore')
# print('dopo la if')
# n = 10
# s = 'ciao'
# citta = 'milano'
# n = 'Simona'
# s2 = s + citta + n
# print(s2)

x = 'ciao'
y = 25
print('la variabile x vale:', x, 'ed è:', type(x))
print('la variabile y vale:', y, 'ed è:', type(y))

MioGatto = 'Tom' #  Pascal Case - preferire negli oggetti
mioGatto = 'Tom' # Camel Case - preferire nelle variabile
mio_gatto = 'Tom' # Snake Case - preferire nelle variabile o campi db

mioGatto, mio_gatto = 'Tom1', 'Tom2'
print(mioGatto)
print(mio_gatto)
print(MioGatto)

# tipi di dato numerici
intero = 15     # int
decimale = 15.5     # float
complesso = 1j      # complex
print('la variabile', intero, 'è', type(intero))
print('la variabile', decimale, 'è', type(decimale))
print('la variabile', complesso, 'è', type(complesso))

intero1 = int(15)
decimale1 = float(15.5)
complesso1 = complex(1j)
print('la variabile', intero1, 'è', type(intero1))
print('la variabile', decimale1, 'è', type(decimale1))
print('la variabile', complesso1, 'è', type(complesso1))

intero2 = int(decimale1)
print('la variabile intero2', intero2, 'è', type(intero2))

# tipi di dato stringa
str = 'ciao'
str2 = 'ciao \na \ntutti'   # \n = newline (nuovo paragrafo)
print(str2)

str3 = """
ciao
a
tutti
"""
print(str3)

# stringhe sono array
nome = 'Federica'
print(nome[1])  # e

frase = 'oggi stiamo lavorando su pycharm scrivendo codice python'
print('la mia frase è lunga', len(frase))

# parola_da_ricercare = input('parola da cercare: ')
# print(parola_da_ricercare, 'esiste',
#       parola_da_ricercare in frase)

# string slicing
print(nome[1:5])    # eder
#   [inizio:fine:step]
print(nome[1:7:2])    # eei
#dato il nome Alessandro stampare solo Ale
nome = 'Alessandro'
print(nome[0:3])
# estrarre "sandro"
print(nome[4:])
print(nome[-6:])
print(nome[-1:-7:-1])   # ordnas (sandro rovesciato)
#   stampare Alessandro rovesciato
print(nome[::-1])
# arrivati slide 30
# esercizi:
# 1_data_type_string_array.py
# 1_data_type_string_slice.py #



