# creare una lista composta dagli elementi pc, monitor, tastiera, mouse
# inserire in posizione 2 gli elementi "porta usb" e "HDD esterno"
# stampare a video la lista
# unire la lista precedente con una nuova lista composta dagli elementi "mac", "pad", "scanner"
# stampare a video la lista
# inserire l'elemento "penna usb" alla fine della lista ottenuta
# stampare a video la lista
# eliminare l'elemento "scanner"
# stampare a video la lista

list1 = ["pc", "monitor", "tastiera", "mouse"]
list1.insert(2, "porta usb")
list1.insert(3, "HDD esterno")
print(list1)

list1.extend(("mac", "pad", "scanner"))
print(list1)

list1.append("penna usb")
print(list1)

# del(list1[8])
# print(list1)

list1.remove("scanner")
print(list1)
