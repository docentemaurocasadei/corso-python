# connettersi ad un database mysql  presente sulla macchina di sviluppo e leggere tutti i record presenti in:
# tabella servizi
# campi  nome, icona e descrizione
# eseguire con python + nomefile e verificare su phpmyadmin se record corrispondono
# fare attenzione a creare il cursore come
# cursore = connessione.cursor(dictionary=True)
# per potere utilizzare i nomi di colonna del dictionary invece che gli indici della tupla
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
	cursore = connessione.cursor(dictionary=True)

	# Comando SQL per l'inserimento del record
	istruzione = "Select * from servizi"

	# Comando SQL per l'estrazione dei record
	cursore.execute(istruzione)

	# Visualizzazione dei record
	risultati = cursore.fetchall()

	for row in risultati:
		print(row['nome'], row['descrizione'])


# Conteggio dei record inseriti print(cursore.rowcount)

except Exception as ex:
	print(ex)



