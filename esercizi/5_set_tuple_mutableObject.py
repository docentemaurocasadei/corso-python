#costruire un esempio su tuple e set per mostrare che sono immutabili (tuple)
# e immmutabili (set) ma con possibilità di aggiungere o rimuovere elementi

#tuple è immutabile, la riassegnazione di 1 solo item da errore
v = (1, 2, 3)
v = (4, 5, 6)
# v[1] = 8 # darebbe errore tupla è immutabile
print(type(v), v, v[1])

#set è mutabile, la riassegnazione di 1 solo item va bene
v = {1, 2, 3}
v = {4, 5, 6}
v.add(7)
