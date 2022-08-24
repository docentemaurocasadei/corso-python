# creare delle variabili che seguano la logica della regola LEGB, ma utilizzare la parola chiave global
# L=local
# E=enclosing
# G=global
# B=builtin

v = 5  # global


def miaF():
    v = 6  # enclosing

    def miaF2():
        global v  # sovrascrive la variabile locale con quella globale
        v = 10

    miaF2()


miaF()
print(v)  # stampa 10 in quanto la keyword global ha sovrascritto la variabile globale
