#creare una lista con gli elementi aventi lo stesso valore tra chiave e valore

d = {"a": "f", "b": "a", "c": "d", "e": "b", "g": "c", "f": "c"}

l = [item for item in d.keys() if item in d.values()]
print(l)

