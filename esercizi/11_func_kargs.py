#creare una funzione che accetta parametri sotto forma di dictionary, stampare le coppie chiave valore
#Marco ha 36
#Silvia ha 28
#Gianni ha 49
#Marta ha 92


def funcKA(**kargs):
    for k,v in kargs.items():
        print(k, "ha", v)

funcKA(Marco = 36, Silvia = 28, Gianni = 49, Marta=92 )