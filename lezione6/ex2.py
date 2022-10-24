# in una gara sono state assegnate le pettorine da 1 a 50
# i primi 3 classificati sono il 15, 25, 38
# ciclare (tramite for) su tutti i partecipanti e stampare i 3 vincitori

vincitori = [15, 25, 38]
vincitori_individuati = 0
for pettorina in range(1,51):
    if pettorina in vincitori:
        print(f'il {pettorina} ha vinto!!')
        vincitori_individuati += 1
    if vincitori_individuati > 2:
        break

vincitori = [15, 25, 38]
podio = list()
for pettorina in range(1,51):
    if pettorina in vincitori:
        print(f'il {pettorina} ha vinto!!')
        podio.append(pettorina)
    if len(podio) > 2:
        break

# eseguire il medesimo esercizio tramite while



# verificare di non sprecare inutilmente tempo e cicli aggiungendo break