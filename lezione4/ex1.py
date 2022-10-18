# simulare di volere iscrivere ad una gara delle persone
# creare una lista con i primi 3 iscritti ovvero:
# Silvia, Sara, Gianni
# successivamente si iscrive Marco usare il metodo append
# successivamente si iscrivono Carlo e Matteo usare il metodo extend
# Silvia si disiscrive _ usare il metodo remove
# ordinare la lista alfabeticamente con il metodo sort
# stampare la lista finale con la funzione print
#

gara = ['Silvia', 'Sara', 'Gianni']
gara.append('Marco')
gara.extend(['Carlo', 'Matteo'])
gara.remove('Silvia')
# del gara['Silvia']
# gara.pop(0)
gara.sort()
print(gara)
