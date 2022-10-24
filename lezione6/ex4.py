# creare una funzione calcola2 che riceve 4 parametri p1, p2, p3, p4
# stampa p1 + p2 + p3 + p4
# chiamare la funzione con i valori:
# 4,5,6,3
# 5,8,3,2

def calcola2(p1,p2,p3,p4):
    print(p1+p2+p3+p4)

calcola2(4,5,6,3)
calcola2(5,8,3,2)

# secondo esempio con parametri dinamici
def somma(*args):
    risultato = 0
    for numero in args:
        risultato += numero
    print(risultato)

somma(4, 5, 6, 3)
somma(5, 8, 3, 2)
somma(5, 8)
somma(5, 8, 8, 9, 3, 4)
#vorrei che la funzione prendesse un parametro per indicare l'operazione
def calcola_dinamica(operatore, *args):
    risultato = 0
    if operatore in ['*', '/']:
        risultato = 1
    for numero in args:
        if operatore == '+':
            risultato += numero
        elif operatore == '-':
            risultato -= numero
        elif operatore == '*':
            risultato *= numero
        elif operatore == '/':
            risultato /= numero
    return risultato


risultato = calcola_dinamica('*', 4, 5, 6, 3)
print('hai totalizzato punti: ', risultato ** 2)
risultato = calcola_dinamica('+', 5, 8, 3, 2)
risultato = calcola_dinamica('-', 5, 8)
risultato = calcola_dinamica('/', 5, 8, 8, 9, 3, 4)