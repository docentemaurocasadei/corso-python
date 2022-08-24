#creare una funzione per stampare a video il valore, tipo e id ti una variabile e chiamarla per ogni datatype conosciuto
def printv(v):
    print(v, "è di tipo", type(v), "ha come indirizzo", id(v))

printv(10)
printv(10.0)
printv(10j)
printv(False)
printv("ciao")
printv([1, 2, 3])
printv((1, 2, 3))
printv({"var1": 1, "var2": 2})
printv({1, 2, 3})

# 10 è di tipo <class 'int'> ha come indirizzo 140728734980032
# 10.0 è di tipo <class 'float'> ha come indirizzo 3140313901008
# 10j è di tipo <class 'complex'> ha come indirizzo 3140306954256
# False è di tipo <class 'bool'> ha come indirizzo 140728734701424
# ciao è di tipo <class 'str'> ha come indirizzo 3140307268720
# [1, 2, 3] è di tipo <class 'list'> ha come indirizzo 3140306868096
# (1, 2, 3) è di tipo <class 'tuple'> ha come indirizzo 3140313710016
# {'var1': 1, 'var2': 2} è di tipo <class 'dict'> ha come indirizzo 3140306821568
# {1, 2, 3} è di tipo <class 'set'> ha come indirizzo 3140313976608
