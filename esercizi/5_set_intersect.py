# avendo i set
# s1 = {'a', 'b', 'c', 'm', 'a'}
# s2 = {'a', 'd', 'm', 'h'}
# creare un nuovo set contenente solo gli elementi comuni

s1 = {'a', 'b', 'c', 'm'}
s2 = {'a', 'd', 'm', 'h'}
s3 = s1.intersection(s2)
print(s3)  # {'m', 'a'}
