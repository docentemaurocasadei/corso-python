# leggere il contenuto del file readme.txt
nome_file = "readme.txt"
f = open(nome_file)
contenuto = f.read()  # legge il contenuto del file
print(contenuto)  # stampa il contenuto

f.seek(0)  # ritorna all'inizio = = primo carattere
print("file letto")

f.close()
print(f.closed)  # True
