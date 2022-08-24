# connettersi ad un database mysql  presente sulla macchina di sviluppo e inserire un record in:
# tabella servizi
# campi  nome, icona e descrizione
# eseguire con python + nomefile e verificare su phpmyadmin se record è presente
import mysql.connector

# Test di connessione a MySQL

try:
	connessione = mysql.connector.connect(
	# Parametri per la connessione
		host="localhost",
		user="root",
		password="",
		db="test"
	)
	# Generazione del cursore
	cursore = connessione.cursor()

	# Comando SQL per l'inserimento del record
	istruzione = "INSERT INTO servizi (nome, icona, descrizione) VALUES (%s, %s, %s)"
	valori = ("Sviluppo Python", "fa-dev", "Sviluppo Python 2")

	# Esecuzone dell'istruzione cursore.execute(istruzione, valori)
	cursore.execute(istruzione, valori)

	# Applicazione delle modifiche
	connessione.commit()

# Conteggio dei record inseriti print(cursore.rowcount)

except Exception as ex:
	print(ex.__cause__)



