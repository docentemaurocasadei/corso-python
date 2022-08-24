# data una lista con le citta bari, ascoli, bologna, milano, firenze, padova, rimini
# creare una lista formata dalle sole città con la a
# utilizzare list comperhension
# stampare la lista ottenuta

list1 = ["bari", "ascoli", "bologna", "milano", "firenze", "padova", "rimini"]
list2 = [item for item in list1 if "a" in item]
print(list2)