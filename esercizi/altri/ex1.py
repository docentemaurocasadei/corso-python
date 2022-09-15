# Scrivi una funzione che prende due numeri come parametro e manda in print il più grande tra i due.
# Per quanto Python disponga di una funzione max(), sei invitato a utilizzare le istruzioni If, Elif ed Else per la scrittura dell'algoritmo

def stampa_max(p1, p2):
    if p1 > p2:
        print('il maggiore è {}'.format(p1))
    else:
        print('il maggiore è {}'.format(p2))


stampa_max(5, 4)