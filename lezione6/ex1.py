# creare una lista contenente i numeri da 1 a 10
# se un numero è pari stamparlo
# se un numero è dispari tramite l'istruzione continue ritornare al controllo del ciclo
# per identificare se numero è pari utilizzare l'operatore %

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# range: 1 parametro è fine
# range: se ci sono 2 parametri il 1 è l'inizio e il 2 è la fine
# range: se ci sono 3 parametri il 1 è l'inizio, il 2 è la fine, il 3 è lo step di aumento
#
for numero in range(10, 20, 3):
    if numero % 2 != 0:
        continue
    print(f'{numero} è pari')
    risultato = numero ** 2
    if risultato > 100:
        print(f'il risultato è {risultato}')

print(range(15))
print(list(range(15)))
