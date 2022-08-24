#creare una variabile di ogni tipo e stamparne il tipo, il contenuto e l'indirizzo di memoria
v = 10
print(v, "è di tipo", type(v), "ha come indirizzo", id(v))

v = 10.0
print(v, "è di tipo", type(v), "ha come indirizzo", id(v))

#complex
v = 10+5j
print(v, "è di tipo", type(v), "ha come indirizzo", id(v))

v = True
print(v, "è di tipo", type(v), "ha come indirizzo", id(v))

v = str("Ciao")
v = "Ciao"
print(v, "è di tipo", type(v), "ha come indirizzo", id(v))

#v = tuple(1,2,3)
v = (1,2,3)
print(v, "è di tipo", type(v), "ha come indirizzo", id(v))

v = list((3,1,2))
v = [3, 1, 2]
print(v, "è di tipo", type(v), "ha come indirizzo", id(v))

v = dict(primo=1, secondo=2, terzo=3)
v = {"primo": 1, "secondo": 2, "terzo": 3}
print(v, "è di tipo", type(v), "ha come indirizzo", id(v))

v = set((3,2,1))
v = {3,2,1}
print(v, "è di tipo", type(v), "ha come indirizzo", id(v))


