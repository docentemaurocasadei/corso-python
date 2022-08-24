# creare un dizionario tramite i dict comprehension dalla lista
# [["marca", "mercedes"],["modello", "slk"],["anno",2022]]

list = [["marca", "mercedes"],["modello", "slk"],["anno",2022]]

dict = {item[0]:item[1] for item in list}

print(dict)