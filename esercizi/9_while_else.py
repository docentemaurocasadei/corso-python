#creare un ciclo while con una variabile valorizzata a 5, quando >15 valorizzare una variabile a True e uscire dal ciclo
i = 5
entratoInElse = False
while i < 15:
    i += 1
else:
    entratoInElse = True #entra quando esce dal ciclo
print(i)
print("entratoInElse: {}".format(entratoInElse))
