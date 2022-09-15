# Scrivi una funzione "moltiplicatrice" che moltiplica tra loro tutti gli elementi di una lista di numeri.
import numpy
def moltiplicatrice(l):
    return numpy.prod(l)


print(moltiplicatrice([5, 4, 6, 8, 22, 5]))
