# creare un oggetto libro che:
# ha una proprietà pagine
# se printato ritorna: "li libro è *****" (*** = titolo)
# se utilizzato il metodo len sull'oggetto libro  deve ritornare il numero di pagine

class Libro:
    def __init__(self, _nome, _pagine):
        self.nome = _nome
        self.pagine = _pagine

    def __str__(self):
        return f"Il libro è {self.nome}"

    def __len__(self):
        return self.pagine


l1 = Libro("Il Nome della Rosa", 576)
l2 = Libro("Via col Vento", 1100)

print(len(l2))
print(l2)
