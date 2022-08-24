# creare una tupla composta dagli elementi "gatto", "cane", "cavallo", "mucca", "gatto", "cane"
# stampare quante volte presente l'elemento gatto
# stampare le posizioni dell'elemento gatto

t1 = ("gatto", "cane", "cavallo", "mucca", "gatto", "cane")
print("gatto è presente:", t1.count("gatto"))

start = 0
for i in range(t1.count("gatto")):
    start = t1.index("gatto", i)
    print("elemento gatto in posizione", start)
    start += 1
