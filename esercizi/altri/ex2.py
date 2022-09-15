# Scrivi una funzione che prende stavolta più numeri come parametro e restituisce il più grande tra loro!

def stampa_max(*args):
    return max(args)


print(f'il maggiore è {stampa_max(5, 4, 6, 9, 2)}')