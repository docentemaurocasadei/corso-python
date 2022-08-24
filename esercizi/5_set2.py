# creare un set, verificare se esiste un elemento inserito dall'utente e in caso rimuoverlo, poi stampare il set a video
# fare l'esercizio sia tramite remove() che tramite discard

# soluzione 1
s = {"a", "b", "c"}
print(s)
item = input('inserire elemento da rimuovere:')
print("**** discard *******")
s.discard(item)
print(s)

#soluzione 2
print("***** remove ******")
s = {"a", "b", "c"}
if item in s:
    s.remove(item)
print(s)
