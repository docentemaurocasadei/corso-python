# avendo i set
# s1 = {'a', 'b', 'c', 'm', 'a'}
# s2 = {'a', 'd', 'm', 'h'}
# comprendere se gli elementi non hanno alcun elemento in comune

s1 = {'a', 'b', 'c', 'm'}
s2 = {'a', 'd', 'm', 'h'}
res = s1.isdisjoint(s2)
print(res)  # False
