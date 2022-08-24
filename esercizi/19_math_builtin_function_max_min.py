# definire una funzione che accetta una serie di numeri e un marametro operation (può valere min o max)
# la funzione stampa il risultato della funzione richiesta
# invocare la funzione sia con min che con max

def min_o_max(*args, operation):
    if operation == "min":
        print(min(args))
    if operation == "max":
        print(max(args))


min_o_max(10, 3, 8, 5, 2, 9, operation="min")

min_o_max(10, 3, 8, 5, 2, 9, operation="max")
