# creare una variabile stringa contenente "oggi è una giornata **** sono ___ gradi xxxx"
# al posto di **** ____ xxxx sostituire ad esempio con calda, 32, centigradi
#utilizzare il metodo format

s = "oggi è una giornata {a} sono {b} gradi {c}"
print(s.format(a="calda", b=32, c="centigradi"))
print(s.format(b=5, c="centigradi", a="fredda"))

