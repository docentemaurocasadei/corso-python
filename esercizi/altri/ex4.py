# Scrivi una funzione a cui viene passato un carattere come parametro, e che ci dice se il carattere è o meno una vocale.

def vocale(v):
    return v in ['a', 'e', 'i', 'o', 'u']


v1 = 'b'
print(f'il carattere {v1} è una vocale: {vocale(v1)}')

v1 = 'e'
print(f'il carattere {v1} è una vocale: {vocale(v1)}')