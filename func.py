def merge(l,m):
l.extend(m)
l.sort()
return l
a=[1,2,5,6,7]
b=[2,4,55,7,9]
print(merge(a,b))
