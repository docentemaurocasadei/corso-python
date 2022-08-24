# utilizzare gli operatori bitwise & | ^ sui numeri 10 e 5
# utilizzare gli operatori bitwise << >> sui numeri 10 e 1

# stampare i risultati

a = 10
b = 5
print("a:", bin(a))
print("b:", bin(b))
print("a & b:", bin(a & b))
print("a | b:", bin(a | b))
print("a ^ b:", bin(a ^ b))
print("a >> b:", bin(a >> 1))
print("a << b:", bin(a << 1))

"""
a: 0b1010
b:  0b101
a & b: 0b0
a | b: 0b1111
a ^ b: 0b1111
a >> b: 0b101
a << b: 0b10100
"""