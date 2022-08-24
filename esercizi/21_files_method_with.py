# leggere il contenuto del file readme.txt utilizzando with
nome_file = "readme.txt"
with open(nome_file) as f:
    for line in f.readlines():  # leggo una riga per volta ritornando una lista
        print(line.strip())  # il metodo strip evita di inserire riga vuota dopo la riga
print(f.closed)  # True
