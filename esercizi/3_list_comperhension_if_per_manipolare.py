# data una lista con le citta bari, ascoli, bologna, milano, roma", firenze, padova, rimini
# creare una lista formata dalle sole città con la a
# utilizzare list comperhension
# in caso la citta sia roma metterla in maiuscolo
# stampare la lista ottenuta

list1 = ["bari", "ascoli", "bologna", "milano", "roma", "firenze", "padova", "rimini"]
list2 = [item if item != "roma" else item.upper() for item in list1 if "a" in item]
print(list2)
