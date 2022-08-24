# creare un nuovo file nominato writeme.txt
# richiedere all'utente di scrivere una nuova riga nel file (tramite funzione input
# fino a che l'utente non inserisce stop
# al termine leggere il contenuto del file inserito
with open('writeme.txt', 'w') as f:
    inp = ''
    while inp.lower() != 'stop':
        inp = input('inserisci riga (scrivere stop per terminare)')
        if inp.lower() != 'stop':
            f.write(f"{inp}\n")
            # f.write("{}\n".format(inp)) potevo fare anche così

with open('writeme.txt', 'r') as f:
    print(f.read())
