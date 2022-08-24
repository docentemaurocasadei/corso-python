#con index
#ricercare la substring "gatto" nella stringa "il gatto ha mangiato le crocchette" e stampare il valore
#ricercare la substring "gatto" nella stringa "il cane ha mangiato le crocchette" e stampare il valore
#ricercare da destra la substring "o" nella stringa "il gatto ha mangiato le crocchette" e stampare il valore

s = "il gatto ha mangiato le crocchette"
print("1 stringa la posizione di gatto:", s.index("gatto")) #1 stringa la posizione di gatto: 3

s2 = "il cane ha mangiato le crocchette"
print("2 stringa la posizione di gatto:", s2.index("gatto")) #2 ValueError: substring not found


s = "il gatto ha mangiato le crocchette"
print("3 stringa la posizione di o da destra:", s.rindex("o")) #exception all'istruzione precedente


