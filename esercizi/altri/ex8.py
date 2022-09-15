# Scrivi una funzione a cui viene passata una parola e riconosce se si tratta di un palindromo (parole che si leggono uguali anche al contrario) oppure meno.
def palidromo(str):
    return str == str[::-1]

parola = 'otto'
risultato = 'non' if not palidromo(parola) else ''
print(f'la parola {parola} {risultato} è un palindromo')

parola = 'ciao'
risultato = 'non' if not palidromo(parola) else ''
print(f'la parola {parola} {risultato} è un palindromo')
