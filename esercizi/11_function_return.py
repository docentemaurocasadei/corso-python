#creare una funzione che accetta un parametro stringa e lo accoda ad una variabile definita
#nello scopo globale, lo ritorna e alla fine stampa la stringa ottenuta
x = "ciao"
def f(a):
    return x + a
print(f("Mauro"))