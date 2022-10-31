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
def inserisci():
    # creo la query INSERT
    query = "INSERT INTO timbrature (codice, nominativo) VALUES(%s, %s)"
    # eseguo la query
    cursore.execute(query, ['cod005', 'Martino Carli'])
    # commit / rollback
    cn.commit()

def leggi():
    try:
        query = "SELECT * FROM timbrature"
        cursore.execute(query)
        risultati = cursore.fetchall()
        for r in risultati:
            print(r['nominativo'])
    except Exception as e:
        print(e)

def aggiorna():
    try:
        #definisco la query
        query = "Update timbrature set nominativo=%s where id=%s"
        #eseguo la query
        cursore.execute(query, ['Marta Bianchi', 1])
        # commit / rollback
        cn.commit()
    except Exception as e:
        print(e)

def elimina():
    try:
        #definisco la query
        query = "DELETE FROM timbrature where id=%s"
        #eseguo la query
        cursore.execute(query, [1])
        # commit / rollback
        cn.commit()
    except Exception as e:
        print(e)



try:
    #creo la connessione
    cn = mysql.connector.connect(
        host="localhost", user="root", password="", db="personale"
    )
    #creo il cursore
    cursore = cn.cursor(dictionary=True)
    # inserisci()
    # aggiorna()
    elimina()
    leggi()

except Exception as e:
    print(e)