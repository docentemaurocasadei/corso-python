# creare una lista composta dagli elementi pc, monitor, tastiera, mouse
# modificare l'elemento monitor con doppio monitor
# stampare a video la lista
# creare una nuova lista composta da tastiera e mouse
# cambiare nella lista principale sia tastiera che mouse in "porta usb" e "HDD esterno"
# stampare a video la lista

list1 = ["pc", "monitor", "tastiera", "mouse"]
list1[1] = "doppio monitor"
print(list1)

list2 = list1[2:4]
print(list2)

list3 = list1[-2:]
print(list3)

list1[2:] = ["porta usb", "HDD esterno"]
print(list1)


