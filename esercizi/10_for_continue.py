# dato un set di valori "banana", "mela", "carota", "pomodoro" stamparne il risultato con un ciclo for
# tramite continue evitare di stampare gli elementi che iniziano con la p
s = {"banana", "mela", "carota", "pomodoro"}
for item in s:
    if item.startswith("p"):
        continue
    print(item)

