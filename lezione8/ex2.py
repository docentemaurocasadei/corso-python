# si richiede di inserire un record richiesto dall'utente
# richiedere tramite input il nominativo
# richiedere tramite input il codice
# connettersi al database
# definire il cursore
# creare la query di inserimento
# eseguire la query
# commit
# leggere la tabella con tutti i record e stampare nome + codice
import mysql.connector
try:
    nominativo = input('inserisci il nominativo:')
    codice = input('inserisci il codice:')
    #creo la connessione
    cn = mysql.connector.connect(
        host="localhost", user="root", password="", db="personale"
    )
    #creo il cursore
    cursore = cn.cursor(dictionary=True)
    # inserisci()
    query = "INSERT INTO timbrature (codice, nominativo) VALUES(%s, %s)"
    # eseguo la query
    cursore.execute(query, [codice, nominativo])
    # commit / rollback
    cn.commit()
    # aggiorna()
    query = "SELECT * FROM timbrature"
    cursore.execute(query)
    risultati = cursore.fetchall()
    for r in risultati:
        print(r['nominativo'],r['codice'])

except Exception as e:
    print(e)