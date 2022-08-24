#definire una variabile fatturato = 50000 e una presenza = 210
# creare una istruzione if al fine di:
# valutare e stampare aumento se presenza > 215 e fatturato > 45.000
# valutare e stampare premio se presenza > 200 e fatturato > 40.000
# valutare e stampare stretta di mano se presenza > 195 e fatturato > 35.000
# valutare e stampare richiamo se presenza < 180 o fatturato < 25.000
# in tutti gli altri casi stampare "nulla da segnalare"

fatturato = 50000
presenza = 210
risultato = "aumento" if presenza > 215 and fatturato > 45000 else "premio" if presenza > 200 and fatturato > 40000 else "stretta di mano" if presenza > 195 and fatturato > 35000 else "richiamo" if presenza < 180 or fatturato < 30000 else "nulla da segnalare"
print(risultato)