# creare una tupla composta dagli elementi "lazio", "lombardia", "veneto", "marche", "emilia romagna"
# assegnare a 2 variabili r1 e r2 le prime 2 regioni e le restante ad una lista r3
# stampare le tre variabili

t1 = ("lazio", "lombardia", "veneto", "marche", "emilia romagna")
r1, r2, *r3 = t1

print("r1", r1)
print("r2", r2)
print("r3", r3)


