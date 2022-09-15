# Scrivi un programma che, passata come parametro una lista di interi, fornisce in output il maggiore tra i numeri contenuti nella lista.

def stampa_max(args):
    return max(args)


print(f'il maggiore è {stampa_max([5, 4, 6, 9, 2])}')