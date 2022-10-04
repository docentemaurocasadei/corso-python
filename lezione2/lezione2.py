#   lancio un messaggio a video
# print('buongiorno')
# v = input('inserisci il valore di v:')
# c = 15
# print('la variabile v vale:', v)

# i = 10      # intero
# f = 10.5    # decimale
# giacomo = 1+5j    # complesso
# print('giacomo è un numero complesso', giacomo)
# print('il tipo di variabile è:', type(giacomo))
# print('intero:', i, ' \ndecimale:', f, ' - complesso:', giacomo)

# la if fa un test
# if condizione :
# if i < 10:
#     print('i è minore di 10')
# else:
#     print('i è maggiore o uguale a 10')

# esercizio: creare un file nominato ex1.py dentro la directory lezione2
# richiedere all'utente (input) un valore
# stampare a video: hai inserito il valore: + valore inserito
# stampare a video 'il valore inserito è di tipo: ' + type() del valore inserito

# v = 'ciao'
# print(v[0:2])
#
# codice_fiscale = "MRARSS90A22H294K"
# # estraete e stampate a video l'anno di nascita
# print(codice_fiscale[6:8])
# # estraete e stampate a video il comune catastale
# print(codice_fiscale[11:15])

# G = proc. giornaliera, M = proc. mensile
# = assegna un valore
# == confronta un valore
# dato_inserito = input('quale procedura? ')
#
#
# if dato_inserito.upper() == 'G':
#     print('ho lanciato la procedura giornaliera')
# elif dato_inserito == 'M':
#     print('ho lanciato la procedura mensile')
# else:
#     print('hai sbagliato scelta')

# semaforo = 'rosso'
# if semaforo == 'verde':
#     print('vai pure')
# elif semaforo == 'giallo':
#     print('rallenta ma passa')
# else:
#     print('fermati')

# .upper() converte in maiuscolo
# .lower() converte in minuscolo
# .strip() cancella gli spazi non significativi
# .replace(vecchio_testo, nuovo_testo) sostituisce uno o più caratteri
# gatto.salta()

# frase = ' il gatto è rosso'
# print(frase)
# stampare la frase in maiuscolo
# print(frase.upper())
# #provate ad utilizzare .lower(), .strip()
# print(frase.lower())
# print(frase.strip())
# print(frase.replace('rosso','bianco'))
# print(frase.count('rosso'))

# creiamo esercizio ex2.py
# dato una frase da richiedere all'utente verificare se presente
# la parola cacca e se presente scrivere "NON PUBBLICABILE" altrimenti "RECENSIONE OK"

# operatori aritmetici +, -, *, /, **, %, //
somma = 5 + 4       # 9
somma = somma * 2   # 18
somma = somma / 6   # 3
somma = somma ** 3  # 27
somma = somma - 7   # 20
somma -= 10         # 10
somma *= 5          # 50
print(somma)

resto = 5 % 2       # 5 / 2 = 2 resto 1
print(resto)
divisione_intera = 18 // 8   #2
print(divisione_intera)

x = 5
y = 6
if x != y:      # != è l'operatore diverso
    print('sono diversi')
else:
    print('sono uguali')

x = 8
y = 6.5
# se uno dei 2 voti è inferiore a 6 sei bocciato
if x < 6 or y < 6:
    print('bocciato')
else:
    print('promosso')

# se entrambi sono uguali o superiori a 6 sei promosso altrimenti bocciato
if x >= 6 and y >= 6:
    print('promosso')
else:
    print('bocciato')

if not x < 6:
    print('in italiano non hai raggiunto la sufficienza')

frase = 'il cane abbaia'
if 'gatto' in frase:    #verifica se presente il carattere o la parola nella frase / lista
    print('c\'è un gatto')

#esercizi per casa:
# 1_data_type_numeric, 1_input, 1_metodi_oggetto_string.py
# 1_string.py, 1_string_find.py, 1_string_isalfanumeric.py, 1_variabili.py
# 2_operatori_aritmetici.py, 2_operatori_comparazione, 2_operatori_logici.py