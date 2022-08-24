# creare una lambda function che elevi al quadrato il numero passato come argomento

def fun(n):
    return lambda a: a * n

print(fun(5)(4)) # richiamo fun e poi visto che ritorna una lambda richiamo con () la lambda
