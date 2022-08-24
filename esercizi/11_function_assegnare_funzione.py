#creare una funzione e provare a:
#assegnarla ad una variabile
#passarla ad una nuova funzione
#ritornarla da una funzione
#memorizzarla in una struttura come list, set, tupla ecc...

def funcEsterna(p):
    def funcInterna():
        return "sono func_interna"
    return funcInterna

def func2():
    return "sono func2"
f1 = func2() #può essere assegnata ad una variabile
print(f1) #sono func_2
f1 = funcEsterna(func2) #può essere passata ad una funzione
print(f1()) #sono func_interna
f1 = funcEsterna(None) #può ritornare
print(f1)
s1 = set((1, 2, funcEsterna(None)())) #{1, 2, 'sono func_interna'}
print(s1)
