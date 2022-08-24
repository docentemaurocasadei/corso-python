# creare un dizionario con i valori:
# "3381234561": "Emanuela"
# "3381234562": "Silvia"
# "3381234563": "Stefano"
# "3381234564": "Marta"
# "3381234564": "Marta Carlini" #sostituisce il precedente
# stampare il dictionary creato con tipo, numero elementi e id in memoria
d1 = {"3381234561": "Emanuela", "3381234562": "Silvia", "3381234563": "Stefano", "3381234564": "Marta", "3381234564": "Marta Carlini"}
print(id(d1), type(d1), len(d1), d1)

d2 = dict({"3381234561": "Emanuela", "3381234562": "Silvia", "3381234563": "Stefano", "3381234564": "Marta Carlini", "3381234564": "Marta"})
print(id(d2), type(d2), len(d2), d2)
