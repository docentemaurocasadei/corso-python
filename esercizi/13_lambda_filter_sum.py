# definire una lista
# l = [10, 12, 'ciao', ['l', 'a'], 14]
#
# tramite sum sommare solo se float o int e stampare il risultato
# realizzare l'esercizio utilizzando list comprehension e funzione filter sia con def che con lambda

l = [10, 12, 'ciao', ['l', 'a'], 14]
l2 = [itm for itm in l if isinstance(itm, float) or isinstance(itm, int)]
print(sum(l2))


# con filter
def filtra(itm):
    if isinstance(itm, float) or isinstance(itm, int):
        return itm


print(sum(filter(filtra, l)))

# con filter e lambda
print(sum(filter(lambda itm: isinstance(itm, float) or isinstance(itm, int), l)))
