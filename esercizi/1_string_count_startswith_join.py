#creare una stringa con contenuto "è una giornata mite, il sole è ombreggiato e ci sono 18 gradi"
#utilizzare su di una stringa i metodi:
#count per contare quante sillabe "so" sono presenti
#split per creare una lista con tutte le parole
#startswith per identificare se inzia con la parola caro
#endswith per identificare se termina con gradi
#definire una tupla ("il", "mio", "nome", "è", "Mauro") e unirla in una stringa


s="è una giornata mite, il sole è ombreggiato e ci sono 18 gradi"
print(s.count("so"))

l = s.split(" ")
print(type(l), l)

print(s.startswith("caro"))

print(s.endswith("gradi"))

t = ("il", "mio", "nome", "è", "Mauro")

print(type(t), t)
print(" ".join(t))
