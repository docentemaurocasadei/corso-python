# creare un set e un frozenset
# testare il metodo copy sia sul set che sul frozenset
# testare il metodo add sia sul set che sul frozenset
# #

s = {1, 2, 3}
f_set = frozenset(s)

print(type(s))
print(type(f_set))

try:
    s.add(4)
    f_set.add(4)  # 'frozenset' object has no attribute 'add'
except Exception as e:
    print(e)
print(s)
print(f_set)
