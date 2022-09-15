# Scrivi una classe libro che ha proprietà: ISBN, titolo e prezzo
# scrivi una classe LibroPresente che eredita Libro e aggiunge la prorieta quantita (in alternativa aggiungere quantita a Libro)
# creare una classe biblioteca con dei metodi
# acquista (accetta ISBN titolo, prezzo e quantita e inserisce il libro in biblioteca se non esiste oppure ne aumenta la quantità se esiste, al termine stampa 'ok libro acquistato: ****' )
# vendi (accetta ISBN e  quantita e diminusce la quantità se esiste, se non esiste o quantità non sufficiente da errore 'ok libro venduto: ****' ))#
# lista (restituisce lista libri con dettagli e giacenze)

class Libro:
    def __init__(self, ISBN, titolo, prezzo):
        self.ISBN = ISBN
        self.titolo = titolo
        self.prezzo = prezzo


class LibroPresente(Libro):
    quantita = 0

    def __init__(self, ISBN, titolo='', prezzo=0.0, quantita=1):
        self.ISBN = ISBN
        self.titolo = titolo
        self.prezzo = prezzo
        self.quantita = quantita

    def __str__(self):
        return f"Libro: {self.ISBN} - Titolo {self.titolo} - Prezzo {self.prezzo} - Quantita {self.quantita}"


class Biblioteca:
    libri = {}

    def acquista(self, ISBN, titolo='', prezzo=0.0, quantita=1):
        if ISBN in self.libri:
            self.libri[ISBN].quantita += quantita
        else:
            l = LibroPresente(ISBN, titolo, prezzo, quantita=quantita)
            self.libri[ISBN] = l
        print(f'ok acquistato :{ISBN}')

    def vendi(self, ISBN, quantita=1):
        if ISBN in self.libri and self.libri[ISBN].quantita >= quantita:
            self.libri[ISBN].quantita -= quantita
            print(f'ok venduto :{ISBN}')
        else:
            print('Libro non presente in sufficiente quantità, impossibile vendere!')

    def lista(self):
        for l in self.libri.values():
            print(l.__str__())


b = Biblioteca()
b.acquista(ISBN='8849413580', titolo='I Promessi Sposi', prezzo=27.75, quantita=2)
b.acquista(ISBN='8808549631', titolo='Chimica.verde', prezzo=18.68, quantita=3)
b.acquista(ISBN='1704976065', titolo='Portami a vedere il mare:', prezzo=13.51, quantita=1)
b.acquista(ISBN='8833751856', titolo='Forse un giorno', prezzo=12.90, quantita=5)
b.acquista(ISBN='8849413580', quantita=2)
b.vendi(ISBN='8849413580', quantita=2)
b.lista()
