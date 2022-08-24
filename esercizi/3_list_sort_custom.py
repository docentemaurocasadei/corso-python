# data una lista con le citta bari, ascoli, bologna, milano, firenze, padova, rimini
# ordinare la lista mettendo prima le citta che contengono la b, poi quelle che contengono la e e infine le altre
# stampare la lista ottenuta

def ordine(v):
    if "b" in v:
        return 1
    elif "e" in v:
        return 2
    else:
        return 3
list1 = ["bari", "ascoli", "bologna", "milano", "firenze", "padova", "rimini"]
list1.sort(key=ordine)
print(list1)
