# creare un dizionario con i valori:
# "3381234561": "Emanuela"
# "3381234562": "Silvia"
# "3381234563": "Stefano"
# "3381234564": "Marta"
# creare una lista con il metodo items()
# stampare la lista


d1 = {"3381234561": "Emanuela", "3381234562": "Silvia", "3381234563": "Stefano", "3381234564": "Marta"}
l1 = d1.items()
print(type(l1), l1)

"""
<class 'dict_items'> dict_items([('3381234561', 'Emanuela'), ('3381234562', 'Silvia'), ('3381234563', 'Stefano'), ('3381234564', 'Marta')])
"""