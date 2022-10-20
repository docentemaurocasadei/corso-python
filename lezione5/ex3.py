# dobbiamo valutare se in base alla temperatura
# una pentola di acqua bolle oppure no
# abbiamo una variabile temperatura e un'altra condizione
# la condizione deve valere
# -fredda se temperatura < 30
# -tiepida se temperatura >=30 e <45
# -calda se temperatura >=45 e <=99
# -bolle se temperatura >=100#

temperatura = 48
condizione = None

if temperatura < 30:
    condizione = 'Fredda'
elif temperatura >=30 and temperatura <45:
    condizione = 'Tiepida'
elif temperatura >=45 and temperatura <99:
    condizione = 'Calda'
elif temperatura >=100:
    condizione = 'Bolle'

print(condizione)