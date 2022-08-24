# creare un set
# della parola "STRINGA"
# tramite set comprehension  e tramite ciclo
# tramite print visualizzare che non sono ordinati

s = {char for char in "STRINGA"}
print(s)

s2 = set()
for c in "STRINGA":
    s2.add(c)
print(s2)

