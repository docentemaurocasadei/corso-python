#creare 1 funzione che accetta un parametro + numero arbitrario di parametri e se di tipo int li somma
def somma(primo, *args):
    tot = 0
    for v in args:
        if isinstance(v, int):
            tot += v
    return tot + primo


res = somma(10, 5, 7, "aaaa", 20)
print(res)
