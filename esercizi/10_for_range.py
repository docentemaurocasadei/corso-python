# utilizzare la funzione range per stampare i numeri da 1 a 10 e con un secondo ciclo da 10 a 1

for i in range(1, 11, 1):
    print(i, end="-")
print(f"\nsecondo ciclo")
for i in range(10, 0, -1):
    print(i, end="-")
