#creare delle variabili che seguano la logica della regola LEGB
#L=local
#E=enclosing
#G=global
#B=builtin

v = 5 #global


def miaF():
    v = 6 #enclosing
    def miaF2():
        v = 7 #local
        return v
    return miaF2()

def miaF3():
    return list

print(miaF())
print(miaF3()) #se provassi con la funzione costruttore list anche se non definita la trova su __builtins__

print(x) #da errore in quanto non è definita ne a livello locale, che enclosing, che globale che builtins


