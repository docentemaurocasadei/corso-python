#creare una funzione che restituisce True se la parola passata è un palindromo, altrimenti False
def palindromo(parola):
    idx_meta = int(len(parola)/2)
    idx_len = int(len(parola))
    meta1 = parola[0:idx_meta]
    meta2 = parola[idx_meta:][::-1]
    return meta1 == meta2

#oppure
def palindromo1(parola):
    return parola == parola[::-1]

print(palindromo("otto"))
print(palindromo("nove"))
print(palindromo("cinque"))
print(palindromo("miagolio"))
print(palindromo("anna"))
