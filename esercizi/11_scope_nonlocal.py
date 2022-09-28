#creare delle variabili che seguano la logica della regola LEGB, ma utilizzare la parola chiave locale
#L=local
#E=enclosing
#G=global
#B=builtin

def miaF():
    v = 6 #enclosing
    def miaF2():
        nonlocal v #sovrascrive la variabile locale con quella globale
        v = 10
    miaF2()
    return v

print(miaF()) #stampa 10 in quanto non anche se la variabile locale sarebbe 6 con la nonlocal sovrascrive quella della enclosing function


