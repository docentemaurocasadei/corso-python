# creare una tupla composta dagli elementi "lazio", "lombardia", "veneto", "marche", "emilia romagna"
# assegnare la tupla ad una list
# sostituire l'elemento in indice 2 con altra regione (nella lista)
# riassegnare la lista alla tupla
# stampare la tupla

t1 = ("lazio", "lombardia", "veneto", "marche", "emilia romagna")
l1 = list(t1)
l1[2] = "abruzzo" #TypeError: 'tuple' object does not support item assignment
t1 = l1
print(t1)



