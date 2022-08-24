#definire una classe che definisce una palla con le proprietà colore, peso e sport
# accettare le proprietà nel metodo __init__
# e come metodo gonfia, sgonfia e rimbalza
# la palla può rimbalzare solo quando è gonfia per cui verificare se gonfia prima di farla rimbalzare

class Palla:
    pallaGonfia = False
    def __init__(self, _colore, _peso, _sport):
        self.colore = _colore
        self.peso = _peso
        self.sport = _sport
    def gonfia(self):
        print("sto gonfiando la palla da ", self.sport)
        self.pallaGonfia = True
    def sgonfia(self):
        print("sto sgonfiando la palla da ", self.sport)
        self.pallaGonfia=False
    def rimbalza(self):
        if self.pallaGonfia:
            print("sto facendo rimbalzare la palla da ", self.sport)
        else:
            print("la palla è sgonfia ")



pBasket = Palla("arancio", "1kg", "basket")
pCalcio = Palla("bianca", "0.8kg", "calcio")
print(pBasket.sport)
pBasket.rimbalza()
pBasket.gonfia()
pBasket.rimbalza()

pBasket.sgonfia()
pBasket.rimbalza()