# creare un ciclo while con una variabile valorizzata a 5, quando >15 valorizzare una variabile a True e uscire dal ciclo
# mettere un break quando i arriva a 10
# verificare che il while non passa dall'istruzione else
i = 5
entratoInElse = False
while i < 15:
    i += 1
    if i >= 10:
        break
else:
    entratoInElse = True  # entra quando esce dal ciclo

print(i)
print("entratoInElse: {}".format(entratoInElse))
