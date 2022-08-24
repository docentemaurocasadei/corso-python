# definire un set con i valori "carta", "plastica", "organico", "indifferenziato", "plastica"
# aggiungere l'elemento "legno" al set
# stampare il set
# aggiungere l'elemento "inerti"
# stampare il set
# eliminare l'elemento "inerti"
# stampare il set
# eliminare l'elemento "metallo" e visualizzare l'errore

s1 = {"carta", "plastica", "organico", "indifferenziato", "plastica"}
s1.add("legno")
print(s1)

s1.add("inerti")
print(s1)

s1.remove("inerti")
print(s1)

s1.remove("metallo")  # KeyError: 'metallo'
print(s1)
