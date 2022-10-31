import locale
# https://bdap-opendata.mef.gov.it/
# aprire il file opendata_bil.csv
# leggere tutte le righe del file
# sommare uno delle colonne (ad esempio OP, oppure OP Erario oppure OP Tesoreria ecc..
# stampare a video la somma ottenuta
somma = 0
with open('opendata_bil.csv', 'r') as f:
    for r in f:
        try:
            l = r.split(';')
            # print(l[14])
            somma += float(l[14]) # OP
        except:
            print('non decimale')

print(somma)
locale.setlocale(locale.LC_ALL, 'it_IT.utf8')
print("{:,f}".format(somma))