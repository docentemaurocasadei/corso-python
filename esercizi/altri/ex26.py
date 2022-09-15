#   Scrivi una funzione che, dato un carattere in ingresso, restituisca in output il codice ASCII associato al carattere passato.
def ascii_num(chr):
    return ord(chr)


inp = input('inserisci un carattere:')
print(f'il codice ascii di {inp} è {ascii_num(inp)}')
