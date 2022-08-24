# avendo i set
# s1 = {'a', 'b', 'c', 'm', 'a'}
# s2 = {'a', 'd', 'm', 'h'}
# creare un nuovo set contenente solo gli elementi non comuni che siano del primo o del secondo set

s1 = {'a', 'b', 'c', 'm'}
s2 = {'a', 'd', 'm', 'h'}
s3 = s1.symmetric_difference(s2)
print(s3)  # {'c', 'b', 'h', 'd'}

