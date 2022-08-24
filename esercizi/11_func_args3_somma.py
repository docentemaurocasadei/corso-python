#creare 1 funzione che accetta un numero arbitrario di parametri e somma a gli interi e quelli pari
def somma(*args):
    tot = 0
    for v in args:
        if isinstance(v, int) and v % 2 == 0:
            tot += v
    return tot


res = somma(10, 5, 7, "aaaa", 20)
print(res)
