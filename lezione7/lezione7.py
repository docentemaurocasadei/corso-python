# from random import randint, shuffle
# import random
import random as rnd
from funzioni import accesso
import datetime
# l = ['carlo', 'sara', 'francesca', 'maria', 'stefano']
# # for
# for nome in l:
#     print(f'il nome è: {nome}')
#
# #while
# print('*****')
# i = 0
# while i < len(l):
#     if l[i] == 'sara':
#         i+=1
#         break
#     print(f'il nome è: {l[i]}')
#     i +=1

#funzioni
# def controlla_nome(nome):
#     if nome == 'stefano':
#         print('bonus di 5 punti')
#     if nome == 'sara':
#         print('bonus di 15 punti')
#     if nome == 'maria':
#         print('penality di 5 punti')
#
# nome1 = input('inserisci il 1 nome da controllare:')
# controlla_nome(nome1)
# nome2 = input('inserisci il 2 nome da controllare:')
# controlla_nome(nome2)


# def somma(p1, p2):
#     print(p1+p2)
#
# somma(1,2)
# somma(5,4)
# somma(p2=6,p1=8)

# def somma(*args):
#     risultato = 0
#     for numero in args:
#         risultato += numero
#     return risultato
#
# ris = somma(5,2)
# print(ris/2)
#
# ris = somma(5,2,4,6,7,8,9,0,1)
# print(ris/2)

# def dividi(p1,p2):
#     return p1 / p2
#
# ris = dividi(5,2)
# print(ris)
# ris = dividi(p2=2, p1=5)
# print(ris)

# def prodotto(divisore, *args,**kargs):
#     print(args)
#     print(kargs)
#     risultato = 1
#     for numero in args:
#         risultato *= numero
#     return risultato / divisore
#
# ris = prodotto(5,8,7,8,9,9,10,p1=10,p4=15)
# print(ris)

# x = 10
# def mia_func():
#     global x
#     x = 5
#     print(f'dentro alla funzione {x}')
#
# mia_func()
# print(f'fuori dalla funzione {x}')
#
# x=5
#
# numero = input('dammi un numero da 1 a 10:')
# n = random.randint(1,10)
# print(f'il numero era questo: {n}?')
#
# l = [1,2,3,4,5]
# rnd.shuffle(l)
# print(l)
#
# if accesso('giovanni', '1234'):
#     print('Benvenuto!')
# else:
#     print('Non sono riuscito a riconoscerti!')
#
# ,rint(datetime.date.today())
# l=[1,5,7,8,10,15,22]
# # print(max(l))
# # print(min([1,5,7,8,10,15,22]))
# # print(round(10.45678,2))
# # print(pow(3,4))
# # print(sum({1,2,3,4,5,6,7,8}))

# numero = input('dammi un numero intero, lo divido per 3:')
# try:
#     print('aaaa')
#     print( int(numero) / 3)
# except ValueError as errore:
#     print('hai inserito un valore non valido!')
# except:
#     print('si è verificato un errore non previsto!')
# print('fine esecuzione')

try:
    with open('budget.csv', 'r') as f:
        risultato = 0
        for linea in f:
            l = linea.split(',')
            importo = float(l[1])
            risultato += importo
    print(risultato)
except Exception as e:
    print('errore durante l\'elaborazione del file budget', e)

# esercizi: 14_libreria_random.py, 14_libreria_math.py, 19_libreria_datetime.py
# 21_files_lineNumber.py, 21_files_method1.py, 21_files_method2.py
# 21_files_method_with.py