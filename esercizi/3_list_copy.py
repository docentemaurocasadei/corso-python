# creare una lista composta dagli elementi pc, monitor, tastiera, mouse
# copiare la lista in una nuova lista2
# modificare il 2 elemento della lista2 con "doppio monitor"

list1 = ["pc", "monitor", "tastiera", "mouse"]
list2 = list1.copy()
# list2 = list1 #così non funzionerebbe in quanto modifichrebbe entrambe le liste
list2[1] = "doppio monitor"


print(list1)
print(list2)
