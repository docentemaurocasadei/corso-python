#creare un dizionario invertendo chiave valore del dizionario d

d = {"a": 0, "b": 1, "c": 2}
d2 = {value:item for item, value in d.items()}
print(d2)

