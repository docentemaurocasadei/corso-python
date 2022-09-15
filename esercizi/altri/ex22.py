# Il ROT-13 è un semplice cifrario monoalfabetico, in cui ogni lettera del messaggio da cifrare viene sostituita con quella posta 13 posizioni più avanti nell'alfabeto.
#
# Scrivi una semplice funzione in grado di criptare una stringa passata, o decriptarla se la stringa è già stata precedentemente codificata.

l1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
      'x', 'y', 'z']
l2 = ['N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
      'K', 'L', 'M']


def cifra(stri):
    str_end = ''
    for c in stri:
        try:
            lettera = l2[l1.index(c.lower())]
            if not c is None:
                str_end += lettera
        except:
            str_end += c
    return str_end


print(cifra('ciao a tutti'))
