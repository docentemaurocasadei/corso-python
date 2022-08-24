# definire un oggetto mouse con
# proprietà colore
# proprietà marca
# marca e colore possono essere valorizzati dall'init
# metodo click_sinistro (stampa a video ho cliccato il pulsante sinistro)
# metodo click_destro (stampa a video ho cliccato il pulsante destro)
# metodo privato __pulisci (stampa sto pulendo il mouse)
# metodo __repr__() che stampa la marca e il colore del mouse
# istanziare 2 mouse uno logitech nero e uno acer bianco
# utilizzare il metodo click_sinistro di uno dei 2 mouse
# invocare il metodo __repr__() di uno dei 2 mouse
# invocare il metodo __pulisci() di uno dei 2 mouse
# fase 2
# creare
# metodo protetto cambia_cursore (richiede come input quale cursore, lo inserisce in una proprietà cursor)
# invocare il metodo cambia_cursore() di uno dei 2 mouse
# stampare la proprietà cursor

#fase 1
# class Mouse:
#     def __init__(self, marca, colore):
#         self.marca = marca
#         self.colore = colore
#
#     def click_sinistro(self):
#         print("ho cliccato il pulsante sinistro")
#
#     def click_destro(self):
#         print("ho cliccato il pulsante destro")
#
#     def __pulisci(self):
#         print("sto  pulendo il mouse")
#
#     def __repr__(self):
#         print(f"sono il {self.marca} {self.colore}")
#
# fase 2
class Mouse:
    cursor = "arrow"

    def __init__(self, marca, colore):
        self.marca = marca
        self.colore = colore

    def click_sinistro(self):
        print("ho cliccato il pulsante sinistro")

    def click_destro(self):
        print("ho cliccato il pulsante destro")

    def __pulisci(self):
        print("sto  pulendo il mouse")

    def __repr__(self):
        print(f"sono il {self.marca} {self.colore}")

    def cambia_cursore(self):
        self.cursor = input("inserisci il nuovo cursore: ")


m1 = Mouse("Logitech", "Nero")
m2 = Mouse("Acer", "Bianco")

m2.click_sinistro()
m1.__repr__()
# m1.__pulisci()  # AttributeError: 'Mouse' object has no attribute '__pulisci'
m1._Mouse__pulisci()  # name mangling: posso accedere al metodo privato
print(m2.cursor)
m2.cambia_cursore()
print(m2.cursor)
