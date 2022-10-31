import mysql.connector
# import random
# import datetime
# funzioni
# def miaF(**p1):
#     print(p1, type(p1))
#
# miaF(p1=10, p2=15, p3=20)

# print(random.randint(1,50))
# print(datetime.datetime.now()) #data e ora attuale
# print(datetime.date.today()) #data di oggi

# with open('testi.txt', 'a', encoding='utf-8') as f:
#     f.write('oggi è il 31/10\n')
#
# with open('testi.txt', 'r', encoding='utf-8') as f:
#     for r in f:
#         print(r, end='')
#
# try:
#     with open('miofile2.txt', 'r', encoding='utf-8') as miof:
#         for r in miof:
#             print(r)
# except:
#     print('c\'è stato un errore!! ') #per rosso \u001b[31m
#
# print('fine codice!')

try:
    #creo la connessione
    cn = mysql.connector.connect(
        host="localhost", user="root", password="", db="personale"
    )
    #creo il cursore
    cursore = cn.cursor(dictionary=True)
    #creo la query INSERT
    query = "INSERT INTO timbrature (codice, nominativo) VALUES(%s, %s)"
    #eseguo la query
    cursore.execute(query,['cod001','Mario Rossi'])
    #commit / rollback
    cn.commit()
except Exception as e:
    print(e)