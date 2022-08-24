# creare una lambda function che riceva un numero arbitrario di parametri e ne ritorni la somma
# usare la funzione sum

fun = lambda *args: sum(args)

print(fun(1, 2, 3, 4))
