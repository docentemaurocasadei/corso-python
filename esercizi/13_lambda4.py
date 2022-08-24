# creare una funzione map()
# la funzione map cicla gli elementi di una collection e ne ritorna un altra con gli elementi variati
# map(function, iterable, ...)
# fare 2 test:
# # 1 per la user defined function utilizzare una lambda function
# # 1 per la user defined function utilizzare una function definita con def
# obiettivo della funzione è restituire gli elementi della lista divisi per 2
# [5, 8, 9, 15, 14, 6]

l = [5, 8, 9, 15, 14, 6]

# prima parte
s = map(lambda item: item / 2, l)
print(list(s))  # [2.5, 4.0, 4.5, 7.5, 7.0, 3.0]


# seconda parte
def dividi_per_2(item):
    return item / 2


print(list(map(dividi_per_2, l)))  # [2.5, 4.0, 4.5, 7.5, 7.0, 3.0]
