# siamo in una scuola e dobbiamo tradurre un voto da numerico a formato alfanimerico
# se 10 voto A
# se 8 voto B
# se 6 voto C
# se 5 voto D
# se 4 voto E
# se 3 voto F
# scriviamo più if .. elif per tale traduzione che dovrà essere salvata
# nella variabile lettera e stampata con print

voto = 8
lettera = None
if voto == 10:
    lettera = 'A'
elif voto == 8:
    lettera = 'B'
elif voto == 6:
    lettera = 'C'
elif voto == 5:
    lettera = 'D'
elif voto == 4:
    lettera = 'E'
elif voto == 3:
    lettera = 'F'
else:
    lettera = 'non so...'

print(lettera)
