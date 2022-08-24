# il fattoriale è il prodotto di tutti i numeri interi positivi inferiori o ugiali al numero dato
# creare una funzione per calcolare il fattoriale del numero dato
# metodo 1: utilizzare un for con ricorsione
# metodo 2: utilizzare un for sena ricorsione

# metodo 1
def calcolaFattoriale(n):
    if n <= 1:
        return 1
    else:
        return n * calcolaFattoriale(n - 1)


v = int(input("richiedi il numero:"))
print(calcolaFattoriale(v))

# metodo 2
ris = 1
for i in range(1, v + 1):
    ris *= i
print(ris)
