# creare un dizionario con i valori:
# "3381234561": "Emanuela"
# "3381234562": "Silvia"
# "3381234563": "Stefano"
# "3381234564": "Marta"
# "3381234564": "Marta Carlini" #sostituisce il precedente
# costruire un dizionario con i numeri di Emanuela e Silvia e il nome "sconosciuto"
# stampare il dictionary creato
d1 = {"3381234561": "Emanuela", "3381234562": "Silvia", "3381234563": "Stefano", "3381234564": "Marta", "3381234564": "Marta Carlini"}

d3 = d1.fromkeys(("3381234561","3381234562"), "sconosciuto")
print(id(d3), type(d3), len(d3), d3)
