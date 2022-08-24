# creare un dizionario con i valori:
# "3381234561": "Emanuela"
# "3381234562": "Silvia"
# "3381234563": "Stefano"
# "3381234564": "Marta"
# "3381234564": "Marta Carlini" #sostituisce il precedente
# richiedere all'utente di inserire un telefono e fornire il nome del telefono indicato
#fare lo stesso con metodo get()

d1 = {"3381234561": "Emanuela", "3381234562": "Silvia", "3381234563": "Stefano", "3381234564": "Marta", "3381234564": "Marta Carlini"}
nome = input("inserisci il telefono:")
print(d1[nome])
