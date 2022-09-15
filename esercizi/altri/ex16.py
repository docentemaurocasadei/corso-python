#   Scrivi una funzione che, dato in ingresso un valore espresso in metri, mandi in print l'equivalente in miglia terrestri, iarde, piedi e pollici.
def convertitore(metri):
    return {
        'metri': metri,
        'yarde': round(metri * 1.09361, ndigits=2),
        'miglia': round(metri * 0.000621371, ndigits=6),
        'piedi': round(metri * 3.28084, ndigits=2),
        'pollici': round(metri * 39.3701, ndigits=2),
    }


print(convertitore(5))