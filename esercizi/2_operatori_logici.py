# utilizzare gli operatori logici and or not sulle condizioni
# 5>4 e 4<5
# 4>5 e 4<5
# 5>4 o 4<5
# 4>5 o 4<5
# "miagola" non è presente in "il cane abbaia"

print("5>4 and 4<5:", 5 > 4 and 4 < 5)
print("4>5 and 4<5:", 4 > 5 and 4 < 5)
print("5>4 or 4<5:", 5 > 4 or 4 < 5)
print("4>5 or 4<5:", 4 > 5 or 4 < 5)

a = "miagola"
b = "il cane abbaia"
print(f"{a} not in {b}:", a not in b)

"""
5>4 and 4<5: True
4>5 and 4<5: False
5>4 or 4<5: True
4>5 or 4<5: True
miagola not in il cane abbaia: True
"""
