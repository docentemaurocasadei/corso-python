# creare un dizionario con i valori:
# "3381234561": "Emanuela"
# "3381234562": "Silvia"
# "3381234563": "Stefano"
# "3381234564": "Marta"
# aggiungere un elemento
# "3381234565": "Carlo"
# stampare la liste delle chiavi
# stampare la liste dei valori


d1 = {"3381234561": "Emanuela", "3381234562": "Silvia", "3381234563": "Stefano", "3381234564": "Marta"}
d1["3381234565"] = "Carlo"
print(d1.keys())
print(d1.values())

"""
dict_keys(['3381234561', '3381234562', '3381234563', '3381234564', '3381234565'])
dict_values(['Emanuela', 'Silvia', 'Stefano', 'Marta', 'Carlo'])
"""