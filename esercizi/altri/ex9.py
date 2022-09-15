# Scrivi una funzione che restituisca la lunghezza di una stringa o lista passata come parametro. In sostanza, seppur presente, provate a scrivere la vostra versione della funzione len()!
def my_len(str):
    conta = 0
    for c in str:
        conta += 1
    return conta


print(my_len('ciao'))
print(my_len([1, 2, 3, 4, 5]))
