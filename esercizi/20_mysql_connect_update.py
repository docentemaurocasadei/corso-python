# connettersi ad un database mysql  presente sulla macchina di sviluppo e aggiornare un record in:
# tabella servizi
# campi  nome, icona, descrizione, id_servizio
# eseguire con python + nomefile e verificare su phpmyadmin se record è stato aggiornato
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
	istruzione = "Update servizi set nome = %s, icona = %s, descrizione = %s WHERE id_servizio = %s"
	valori = ("Sviluppo PHP", "fa-dev", "Sviluppo PHP descrizione 4", 8)

	# Esecuzone dell'istruzione cursore.execute(istruzione, valori)
	cursore.execute(istruzione, valori)

	# Applicazione delle modifiche
	connessione.commit()

# Conteggio dei record inseriti print(cursore.rowcount)

except Exception as ex:
	print(ex.__repr__())



