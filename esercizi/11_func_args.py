#creare 1 funzione che accetta un numero arbitrario di parametri e se di tipo int li somma
def somma(*args):
    tot = 0
    for v in args:
        if isinstance(v, int):
            tot += v
    return tot


res = somma(10, 5, 7, "aaaa", 20)
print(res)
