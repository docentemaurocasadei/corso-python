# avendo i set
# s1 = {'a', 'b', 'c', 'm', 'a'}
# s2 = {'a', 'd', 'm', 'h'}
# creare un nuovo set contenente gli elementi di entrambi i set

s1 = {'a', 'b', 'c', 'm'}
s2 = {'a', 'd', 'm', 'h'}
s3 = s1.union(s2)
print(s3)  # {'d', 'm', 'a', 'b', 'c', 'h'}

