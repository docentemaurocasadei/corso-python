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

def prodotto(divisore, *args,**kargs):
    print(args)
    print(kargs)
    risultato = 1
    for numero in args:
        risultato *= numero
    return risultato / divisore

ris = prodotto(5,8,7,8,9,9,10,p1=10,p4=15)
print(ris)





