#scrivere una funzione e commentarla con la sintassi docstring
def somma(*args):
    """somma più argomenti restituendo il risultato"""
    tot = 0
    for n in args:
        tot +=n
    return tot

print(somma.__doc__)
print(somma(3, 4, 5))
