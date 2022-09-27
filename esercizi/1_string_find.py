#ricercare con metodo find la substring "gatto" nella stringa "il gatto ha mangiato le crocchette" e stampare la posizione
#ricercare con metodo find la substring "gatto" nella stringa "il cane ha mangiato le crocchette" e stampare la posizione
#ricercare con metodo rfind da destra la substring "o" nella stringa "il gatto ha mangiato le crocchette" e stampare la posizione

s = "il gatto ha mangiato le crocchette"
print("1 stringa la posizione di gatto:", s.find("gatto")) #1 stringa la posizione di gatto: 3

s2 = "il cane ha mangiato le crocchette"
print("2 stringa la posizione di gatto:", s2.find("gatto")) #2 stringa la posizione di gatto: -1

s = "il gatto ha mangiato le crocchette"
print("3 stringa la posizione di o da destra:", s.rfind("o")) #1 stringa la posizione di gatto: 3


