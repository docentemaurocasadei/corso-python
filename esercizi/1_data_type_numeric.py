# creare una variabile per ogni tipo di dato numerico in python (int, float, complex)
# sommare un numero reale o un numero immaginario alle variabili create
# stampare il risultato comprensivo del tipo di dato finale

#modalità 1
a = 10
b = 5.6
c = 5+6j

a, b, c = 10, 5.6, 5+6j

a += 5
b += 9j
c += 2

print("a", type(a), a)
print("b", type(b), b)
print("c", type(c), c)