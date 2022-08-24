#In Python, la parte immaginaria può essere espressa semplicemente aggiungendo una j o J dopo il numero
# creare alcuni numeri complessi come:
# 2-3j
# 1j
# 0j
# 5-9j
# 2+3j
# di alcuni numeri visualizzare il tipo tramite la funzione builtin type()
# di un numero visualizzare la parte immaginaria tramite la proprietà .imag

z = complex(2, -3)
print(z)

z = 1j
print(z)

z = complex()
print(z)

z = complex('5-9j')
print(z)

a = 2+3j

print(a.imag)

"""
risultati
(2-3j)
1j
0j
(5-9j)
3.0
"""