#creiamo esercizio ex2.py
#dato una frase da richiedere all'utente verificare se presente
#la parola cacca e merda e se presente scrivere "NON PUBBLICABILE" altrimenti "RECENSIONE OK"

# ho mangiato veramente male... una cacca
v = input('inserisci il la recensione:')
# num_parole_bloccate = v.count('cacca')
num_parole_bloccate = v.count('cacca')
num_parole_bloccate1 = v.count('merda')
if num_parole_bloccate > 0 or num_parole_bloccate1>0:
    print('NON PUBBLICABILE')
else:
    print('RECENSIONE OK')

v = input('inserisci il tuo telefono:')
# mettere un test che grazie a .isdigit() verifica se è stato
# inserito un numero e stampa "CORRETTO" oppure "ERRATO"
if(v.isdigit() == True):
    print('Corretto')
else:
    print('Errato')
print(v.isdigit())


