#
# creare una funzione che accetta nomi, cognomi e altri parametri tramite kwargs li stampa in maiuscolo con il nome del paramentro
# risultato
# nome: MARCO cognome: GATTI cellulare: 3471234567
# ****
# nome: SILVIA cognome: BIANCHI cellulare: 3471234561 telefono: 0541123456
# ****
# nome: EMANUELA cognome: SARTI telefono: 0722123451
# ****
# nome: RAFFAELLA cognome: STEFANINI telefono: 0721123456
# ****

def printRiferimenti(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v.upper()}", end=" ")
    print(f"\n****")


printRiferimenti(nome="Marco", cognome="Gatti", cellulare="3471234567")
printRiferimenti(nome="Silvia", cognome="Bianchi", cellulare="3471234561", telefono="0541123456")
printRiferimenti(nome="Emanuela", cognome="Sarti", telefono="0722123451")
printRiferimenti(nome="Raffaella", cognome="Stefanini", telefono="0721123456")
