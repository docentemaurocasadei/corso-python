#definire un oggetto con un:
#attributo pubblico
#attributo privato
#attributo accessibile ma sconsigliato l'accesso

class Aula:
    def __init__(self):
        self.nome = "mio nome"
        self._nome = "mio nome accessibile ma sconsigliato"
        self.__nome= "mio nome non accessibile a causa del name handling"

a = Aula()
print(a.nome) #ok
print(a._nome) #ok ma sconsigliato accesso diretto
#print(a.__nome) #errore
print(a._Aula__nome) # name mangling istanza . _ NomeClasse nomeAttributo
